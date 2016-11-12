#!/usr/bin/env python
# -*- coding: utf-8 -*-

from socket import *

def scanTCP(IP):
    for i in range(17, 1025): # Scan des is 17 à 1025
        client = socket(AF_INET, SOCK_STREAM) # initialisation de la connection

        resultat = client.connect_ex((IP, i)) # Connection au port

        port_name = "NONE"

        # Attribition des noms de port
        if i == 17:
            port_name = "QOTD"
        elif i == 18:
            port_name = "Message Sent Protocol"
        elif i == 19:
            port_name = "CHARGEN"
        elif i == 20:
            port_name = "FTP data transfer"
        elif i == 21:
            port_name = "FTP control"
        elif i == 22:
            port_name = "SSH"
        elif i == 23:
            port_name = "Telnet"
        elif i == 25:
            port_name = "SMTP"

        if resultat == 0 and port_name == "NONE":
            print "[-] PORT %d: OUVERT" % (i)
        elif resultat == 0 and port_name != "NONE":
            print "[-] PORT %s %d: OUVERT" % (port_name, i)
        client.close() # Arret de la connection
