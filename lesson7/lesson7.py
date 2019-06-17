import socket
import views


class WebServer:
    def __init__(self, port):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.websocket = ("127.0.0.1", port)
        self.urls = {"/": views.html(), "/about": "about", }

    def parse_req(self, request):
         return request.split(" ")[1]
    def get_headers(self, url):
        if url in self.urls:
             return "HTTP/1.1 200 OK\n\n", 200
        else:
             return "HTTP/1.1 404 Not found\n\n", 404
    def get_content(self, url, code):
         if code == 200:
            return self.urls[url]
         elif code == 404:
             return "<h1>Page not found</h1>"
    def server_response(self, requests):
        url = self.parse_req(requests)
        headers, code = self.get_headers(url)
        content = self.get_content(url, code)
        return headers + content
    def start(self):
        self.server_socket.bind(self.websocket)
        self.server_socket.listen()
        while True:
            client_socket, address = self.server_socket.accept()
            request = client_socket.recv(2048)
            response = self.server_response(request.decode())
            print(address)
            print(request)
            client_socket.sendall(response.encode())
            client_socket.close()


WebServer(9998).start()