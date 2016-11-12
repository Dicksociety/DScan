#!/usr/bin/env python
# -*- coding: utf-8 -*-

from socket import *

def scanTCP(IP):
    for i in range(17, 1025): # Scan des ports 17 à 1025
        client = socket(AF_INET, SOCK_STREAM) # Initialisation de la connection

        resultat = client.connect_ex((IP, i)) # Connection au port "i"

        if resultat == 0: # Si la connection a reussi alors affiché :
            print "[-] PORT %d: OUVERT" % (i)
        client.close() # Arret de la connection
