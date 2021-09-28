#!/usr/bin/python3

#Escaner de puertos con opcion de crear un fichero

import sys
import traceback
import socket

default_ports = [20, 21, 22, 25, 53, 80, 139, 443, 1080, 3128, 8080, 8081]
try:
    if len(sys.argv) > 3:
        if sys.argv[3] == "-O":
            option = sys.argv[3]
            text = sys.argv[4]
            init_port, end_port = sys.argv[1].split("-")
            ip_result = socket.gethostbyname(sys.argv[2])
            print("Iniciando escaneo de la ip {} ...".format(ip_result))
            for port in range(int(init_port), int(end_port)):
                puerto = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                puerto.settimeout(5000)
                conexion = puerto.connect_ex((ip_result, port))
                if conexion == 0:
                    print("PORT", port, "OPEN")
                    puerto.close()
            file = open("/home/rosin/Desktop/Hacking/Intecssa/Python/{}".format(text), "x")
            file.write("IP:".format(str(ip_result)))
            for i in range(int(init_port), int(end_port)):
                file.write("port: ")
                file.write((str(port))
            file.close()

    elif len(sys.argv) > 2:
        init_port, end_port = sys.argv[1].split("-")
        ip_result = socket.gethostbyname(sys.argv[2])
        print("Iniciando escaneo de la ip {} ...".format(ip_result))
        for port in range(int(init_port), int(end_port)):
            puerto = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            puerto.settimeout(5000)
            conexion = puerto.connect_ex((ip_result, port))
            if conexion == 0:
                print("PORT", port, "OPEN")
                puerto.close()

    elif len(sys.argv) > 1:
        ip_result = socket.gethostbyname(sys.argv[1])
        print("Iniciando escaneo de la ip {} ...".format(ip_result))
        for port in default_ports:
            puerto = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            puerto.settimeout(5000)
            conexion = puerto.connect_ex((ip_result, port))
            if conexion == 0:
                print("PORT", port, "OPEN")
                puerto.close()

except:
    traceback.print_exc()
    print("USO 'ej8.py <INITPORT-ENDPORT> <IP-HOST> <OPCION> <Nombre_archivo>'")
