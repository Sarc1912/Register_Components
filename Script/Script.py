from mimetypes import init
import psutil
import platform
import sys
from datetime import datetime
import socket
import psycopg2
import getpass



class RecolectarDatos():
    def __init__(self):
        uname = platform.uname()
        
        conexion = psycopg2.connect(database="postgres",user ="postgres",password="admin",host="localhost",port="5432")
        self.nombreMaquina = uname.node
        self.arquitectura = uname.machine
        self.sistema = uname.system+" "+uname.release
        self.procesador = uname.processor
        self.nucleos = psutil.cpu_count(logical=True)
        self.ram = self.get_size(psutil.virtual_memory().total)
        self.username = getpass.getuser()
        
        
        self.partitions = psutil.disk_partitions()
        for partition in self.partitions:
            try:
                self.partition_usage = psutil.disk_usage(partition.mountpoint)
            except PermissionError:
                continue
            self.disco = self.get_size(self.partition_usage.total)
        
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8",80))
        self.ip = s.getsockname()[0]
        
        try:
            with conexion:
                with conexion.cursor() as cursor:
                    datos = (self.username,self.nombreMaquina,self.ip, self.disco,self.procesador,self.nucleos,self.ram,self.sistema,self.arquitectura)
                    dato = (self.nombreMaquina,)
                    ejecutar = sentencia = " SELECT EXISTS(SELECT * from componentes WHERE machinename=%s)"
                    cursor.execute(sentencia,dato)
                    registros = cursor.fetchall()
                    
                    if registros == [(True,)]:
                        sentencia = "Delete From componentes WHERE machinename = %s"
                        ejecutar
                        print("Registro eliminado")
                        sentencia ="""INSERT INTO componentes(username,machinename,ip,disksize,processor,cores,ram,os,architecture)
                        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                        cursor.execute(sentencia,datos)
                        print("Registro Exitosox2")
                    else:
                        sentencia ="""INSERT INTO componentes(username,machinename,ip,disksize,processor,cores,ram,os,architecture)
                        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                        cursor.execute(sentencia,datos)
                        print("Registro Exitoso")
                    
                    #cursor.execute(sentencia,datos)
        except Exception:
            print(Exception)
        finally:
            conexion.close()


    
    
    #Funcion para Convertir de Bites a gb
    def get_size(self, bytes, suffix="B"):
        factor = 1024
        for unit in ["", "K", "M", "G", "T", "P"]:
            if bytes < factor:
                return f"{bytes:.2f}{unit}{suffix}"
            bytes /= factor



guardarDatos = RecolectarDatos()







