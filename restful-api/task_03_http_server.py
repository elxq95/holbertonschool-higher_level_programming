#!/usr/bin/python3

import http.server
import socketserver
import json

# Define a request handler by subclassing BaseHTTPRequestHandler
class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    
    # Handle GET requests
    def do_GET(self):
        # Check the path to serve different content
        if self.path == '/':
            # Send response status code
            self.send_response(200)
            # Send headers
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            # Send the body of the response
            self.wfile.write(b"Hello, this is a simple API!")
        
        elif self.path == '/data':
            # Send JSON response for /data endpoint
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            # Sample data
            data = {"name": "John", "age": 30, "city": "New York"}
            # Write the JSON data as bytes
            self.wfile.write(json.dumps(data).encode())

        elif self.path == '/status':
            # Check API status
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            status = {"status": "OK"}
            self.wfile.write(json.dumps(status).encode())
        
        else:
            # Handle undefined endpoints (404 error)
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            error_message = {"error": "Endpoint not found"}
            self.wfile.write(json.dumps(error_message).encode())

# Set the port number and start the server
PORT = 8000
Handler = SimpleHTTPRequestHandler

# Start the HTTP server on localhost:8000
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
