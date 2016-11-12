#!/usr/bin/env python
# -*- coding: utf-8 -*-

from socket import *
from tcp import *

if __name__ == '__main__':
    cible = raw_input("Entrez l'hôte à scanner : ")
    cibleIP = gethostbyname(cible) # Conversion de l'hôte en adresse IP
    print "[-] Demarrage du scan pour : ", cibleIP
    scanTCP(cibleIP) # Fonction situé dans le dossier tcp.py
