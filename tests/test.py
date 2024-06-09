import unittest
import socket
import threading
import time

from app.app import main


class TestTCPHandler(unittest.TestCase):
    def test_handle(self):
        print("Starting server")

        # Set up a TCP server in a separate thread
        server_thread = threading.Thread(target=main, daemon=True)
        server_thread.start()
        time.sleep(1)  # Wait for the server to start

        # Connect a client to the server
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('127.0.0.1', 65432))

        # Send data to the server and receive response
        client_socket.sendall(b'Test data')
        response = client_socket.recv(1024).decode()

        # Close the client socket
        client_socket.close()

        # Assert that the server responded correctly
        self.assertEqual(response, 'Test data')


if __name__ == '__main__':
    unittest.main()
