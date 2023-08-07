import http.server
import socketserver
import sys
from get_ip import get_server_ip

# Parse command line arguments or ask for user input
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = input("Please select a file: ")

if len(sys.argv) > 2:
    port = int(sys.argv[2])
else:
    port = int(input("Please select a port: ") or "1337")

if len(sys.argv) > 3:
    verbose = sys.argv[3].lower() in ['true', 'yes', '1']
else:
    verbose = input("Verbose mode on? y/n: ").lower() in ['y', 'yes']

# Create a custom handler to always serve the same file
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if verbose:
            print(f'Incoming connection from {self.client_address}')
        self.path = '/' + filename
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Create server
with socketserver.TCPServer(("0.0.0.0", port), MyHandler) as httpd:
    print(f"Serving {filename} at http://{get_server_ip()}:{port}")
    httpd.serve_forever()

