import requests

HOSTNAME = 'http://localhost:8003'
MESSAGES_PATH = '/messages'

messages = ''

def ecrireUnMessage () :
    message = raw_input('Entrez votre message : ')
    return message

def envoyerUnMessageAuServeur (message) :
    r = requests.post(HOSTNAME + MESSAGES_PATH, data = message)

def recupererLesMessagesDuServeur () :
    r = requests.get(HOSTNAME)
    messages = r.text

def afficherLesMessages () :
    print(messages)

message = ecrireUnMessage()
envoyerUnMessageAuServeur(message)
recupererLesMessagesDuServeur()
