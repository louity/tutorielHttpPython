#!/usr/bin/env python
# -*- coding: utf-8 -*-
from BaseHTTPServer import HTTPServer
from BaseHTTPServer import BaseHTTPRequestHandler
from subprocess import call

PORT = 8003
FILE_PREFIX = '.'

messages = ['SERVEUR DE MESSAGERIE']
separator = '\n'
description = 'COMPLETER AVEC LA DESCRIPTION DE MON SERVICE'

def respondToRequest (request, code, output) :
    request.send_response(response_code)
    request.send_header('Content-type', 'text')
    request.end_headers()
    request.wfile.write(output)

def getRequestBody (request) :
    content_length = int(request.headers.getheader('content-length', 0))
    post_body = request.rfile.read(content_length)
    return post_body

class MyHandler(BaseHTTPRequestHandler):

    # gestion des requetes HEAD
    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    # gestion des requetes GET
    def do_GET(self):
        if self.path == '/description':
            response_code = 200
            output = description
        elif self.path == '/ADEFINIR':
            response_code = 200
            output = 'ADEFINIR'
        else:
            response_code = 404
            output = 'path /descrition describes available routes'

        # respond to the request
        respondToRequest(self, response_code, output)

    # getion des requestes POST
    def do_POST(self):
        # get the posted body
        post_body = getRequestBody(self)
        if self.path == '/adefinir':
            # a definir
            response_code = 200
            output = ''
        else:
            response_code = 404
            output = 'path /descrition describes available routes'

        # respond to the request
        respondToRequest(self, response_code, output)


server = HTTPServer(('localhost', PORT), MyHandler)
print('server listening on port', PORT)

server.serve_forever()

