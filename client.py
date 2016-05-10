#!/usr/bin/env python
# -*- coding: utf-8 -*-# une librairie pour faire des requetes HTTP
import requests

# adresse du seveur
HOSTNAME = 'A REMPLIR'
# chemin des messages dans le serveur
MESSAGES_PATH = '/messages'

messages = ''

# fonction qui demande l'ecriture d'un message dans la console
def ecrireUnMessage () :
    message = raw_input('Entrez votre message : ')
    return message

# fonction qui envoie le message au serveur
def envoyerUnMessageAuServeur (message) :
    r = requests.post(HOSTNAME + MESSAGES_PATH, data = message)

# fonction qui recupère tous les messafes du serveur
def recupererLesMessagesDuServeur () :
    global messages
    r = requests.get(HOSTNAME)
    messages = r.text

# fonction qui affiche les messages dans la console
def afficherLesMessages () :
    global messages
    print(messages)

message = ecrireUnMessage()
envoyerUnMessageAuServeur(message)
recupererLesMessagesDuServeur()
