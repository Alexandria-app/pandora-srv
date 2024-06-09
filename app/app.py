import socketserver

from app.script_loader import ScriptLoader


class TCPHandler(socketserver.BaseRequestHandler):
    script_loader = ScriptLoader()

    def handle(self):
        print(f"Connected by {self.client_address}")
        while True:
            data = self.request.recv(1024)
            if not data:
                break

            print(f"Received from {self.client_address}: {data.decode()}")
            self.request.sendall(data)


def main():
    HOST, PORT = '127.0.0.1', 65432
    with socketserver.ThreadingTCPServer((HOST, PORT), TCPHandler) as server:
        print(f"Server listening on {HOST}:{PORT}")
        server.serve_forever()


if __name__ == '__main__':
    main()
