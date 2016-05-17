import requests

HOSTNAME = 'http://localhost:8003'
MESSAGES_PATH = '/messages'

separateur = '\n'
messages = []
numeroDuDernierMessageAffiche = 0

def ecrireUnMessage () :
    message = raw_input('Entrez votre message : ')
    return message

def envoyerUnMessageAuServeur (message) :
    r = requests.post(HOSTNAME + MESSAGES_PATH, data = message)

def recupererLesMessagesDuServeur () :
    global messages
    r = requests.get(HOSTNAME)
    messages = r.text.split('\n')

def afficherLesMessages () :
    global messages, numeroDuDernierMessageAffiche
    print(separateur.join(messages))
    numeroDuDernierMessageAffiche = len(messages) - 1

def affichersLesNouveauxMessages () :
    global messages, numeroDuDernierMessageAffiche
    derniersMessages = messages[numeroDuDernierMessageAffiche:]
    print(separateur.join(derniersMessages))
    numeroDuDernierMessageAffiche = len(messages) - 1

continuerAEcrireUnMessage = True

while continuerAEcrireUnMessage :
    message = ecrireUnMessage()
    if (len(message) == 0):
        continuerAEcrireUnMessage = False
    else:
        envoyerUnMessageAuServeur(message)
    recupererLesMessagesDuServeur()
    affichersLesNouveauxMessages()

