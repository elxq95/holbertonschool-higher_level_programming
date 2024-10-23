#!/usr/bin/python3
"""This module handles a method to fetch posts
from JSONPlaceholder using requests.get()
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        res_data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Hello, this is a simple API!')
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(res_data).encode('utf-8'))
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'OK')
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Endpoint not found')

httpd = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()
