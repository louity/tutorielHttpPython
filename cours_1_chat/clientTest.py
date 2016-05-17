#!/usr/bin/env python
# -*- coding: utf-8 -*-# une librairie pour faire des requetes HTTP
import requests

# adresse du seveur
HOSTNAME = 'http://www.google.fr'

r = requests.get(HOSTNAME)
print(r.text)
