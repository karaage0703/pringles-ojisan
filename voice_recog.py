# -*- coding: utf-8 -*-
import socket
import xml.etree.ElementTree as ET
import subprocess
import time
import read_spi_adc as adc
import jtalk

host = 'localhost'
port = 10500
 
clientsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsock.connect((host, port))

sf = clientsock.makefile('rb')

def measure():
    adc_val = adc.convertVolts(adc.readAdc(0))
    print("adc_volt=" + str(adc_val))
    if 0 < adc_val < 1.8:
        print("omoi")
        jtalk.jtalk("たくさんのこってる")
    elif 1.8 <= adc_val < 2.5:
        print("maamaa")
        jtalk.jtalk("はんぶんくらいのこってる")
    else:
        print("karui")
        jtalk.jtalk("からっぽ")

while True:
    line = sf.readline().decode('utf-8')
    if line.find('WHYPO') != -1:
        print line
        if line.find(u'C1') != -1:
            print("measure")
            measure()
        elif line.find(u'C2') != -1:
            print("oshaberi")
            # hello()
        elif line.find(u'C3') != -1:
            print("unkodeta")
            # hello()

