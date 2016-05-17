#!/usr/bin/env python
# -*- coding: utf-8 -*-# une librairie pour faire des requetes HTTP
import requests

# adresse de mon serveur
LOCALHOSTNAME = 'http://localhost'

# test du path /desciption
path = '/description'
r = requests.get(HOSTNAME + ':' + PORT + '/description')
print(r.code)
print(r.text)
