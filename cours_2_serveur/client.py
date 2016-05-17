#!/usr/bin/env python
# -*- coding: utf-8 -*-# une librairie pour faire des requetes HTTP
import requests

# adresse du seveur
HOSTNAME = 'A COMPLETER'
path = '/description'
r = requests.get(HOSTNAME + path)
print(r.code)
print(r.text)
