#!/usr/bin/env python
# -*- coding: utf-8 -*-# une librairie pour faire des requetes HTTP
import requests

# adresse de mon serveur
LOCALHOSTNAME = 'http://localhost'
PORT = 8003

# test du path /desciption
path = '/description'

adress = str(LOCALHOSTNAME) + ':' + str(PORT) + '/description'
print(adress)

r = requests.get(adress)
print(r.text)
