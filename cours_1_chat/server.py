#!/usr/bin/env python
# -*- coding: utf-8 -*-
from BaseHTTPServer import HTTPServer
from BaseHTTPServer import BaseHTTPRequestHandler
from subprocess import call

PORT = 8003
FILE_PREFIX = "."

messages = ['SERVEUR DE MESSAGERIE']
separator = '\n'

class MyHandler(BaseHTTPRequestHandler):

    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        # generate data
        output = separator.join(messages) + separator

        # respond to the request
        self.send_response(200)
        self.send_header("Content-type", "text")
        self.end_headers()
        self.wfile.write(output)

    def do_POST(self):
        if self.path == "/messages":
            # get the data
            response_code = 200
            content_len = int(self.headers.getheader('content-length', 0))
            post_body = self.rfile.read(content_len)
            # handle the data
            messages.append(post_body)
            call(["say", "-v", "Anna", post_body])
            output = post_body
        else:
            response_code = 404
            output = "you must post on /message"

        # respond to the request
        self.send_response(200)
        self.send_header("Content-type", "text")
        self.end_headers()
        self.wfile.write(output)



server = HTTPServer(("localhost", PORT), MyHandler)
print('server listening on port', PORT)

server.serve_forever()

