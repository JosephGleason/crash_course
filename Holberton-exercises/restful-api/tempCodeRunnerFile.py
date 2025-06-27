#!/usr/bin/python3

# Imports the tools to build a custom HTTP server.
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# defining a custom request handler class.
# It inherits from BaseHTTPRequestHandler, 
# which gives you methods to handle things like GET/POST and to respond to clients.
class Handler(BaseHTTPRequestHandler):
    #overrides the method that runs whenever the server receives a GET request
    def do_GET(self):
        #"/" means the root of the site.
        if self.path == "/":
            #Sends an HTTP 200 OK status — tells the browser “this request succeeded.”
            self.send_response(200)
            #Adds a header: “the body I’m sending is plain text.”
            self.send_header("Content-Type", "text/plain")
            #Tells the browser: “headers are done — body is about to start.”
            self.end_headers()
            #Sends the actual response message to the client in bytes.
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
           self.send_response(200)
           self.send_header("Content-Type", "application/json")
           self.end_headers()
           data = {"name": "John", "age": 30, "city": "New York"}
           json_string = json.dumps(data)
           self.wfile.write(json_string.encode('utf-8'))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            response = "Endpoint not found"
            self.wfile.write(response.encode('utf-8'))

if __name__ == "__main__":
    server = HTTPServer(("localhost", 8000), Handler)
    print("Starting server at http://localhost:8000")
    server.serve_forever()
