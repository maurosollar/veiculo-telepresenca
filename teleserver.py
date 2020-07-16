#! /usr/bin/env python
# -*- coding: latin-1 -*-
# Controle do veículo de Tele Presença
# Autor: Mauro Costa Sollar
# 16/07/2020

import socket
import serial

ser = serial.Serial('/dev/serial0', baudrate=9600, bytesize=8, parity="N", stopbits=1, timeout=2, xonxoff=0, rtscts=0)

UDP_IP = "0.0.0.0"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    print ser.readline()
    data, addr = sock.recvfrom(1024)
    print "received message:",  data
    comando = data[0:1]
    print "Comando: (" + comando + ")"
    # Envia comando via serial para o kit das rodas Mecanum qual tem um Arduino como controlador
    ser.write(comando)
