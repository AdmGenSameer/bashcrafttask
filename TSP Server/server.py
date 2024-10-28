import socket
import logging
from datetime import datetime

# Set up logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class TCPServer:
    def __init__(self, host='0.0.0.0', port=8080):
        """Initialize the server with a specified host and port."""
        self.host = host
        self.port = port
        self.socket = None

    def setup_socket(self):
        """Create and configure the server socket."""
        try:
            # Initialize the socket with IPv4 and TCP settings
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Enable the reuse of the address
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            # Bind the socket to the host and port
            self.socket.bind((self.host, self.port))
            # Start listening for incoming connections
            self.socket.listen(1)
            logging.info(f"Server is listening on {self.host}:{self.port}")
        except Exception as e:
            logging.error(f"Socket setup failed: {e}")
            raise

    def run(self):
        """Start the server and manage incoming connections."""
        self.setup_socket()
        
        try:
            while True:
                # Wait for an incoming connection
                client_socket, client_address = self.socket.accept()
                
                # Log details about the connection
                logging.info(f"Connected by client at {client_address[0]}:{client_address[1]}")
                
                # Immediately close the connection after logging
                client_socket.close()
                logging.info(f"Connection closed for {client_address[0]}:{client_address[1]}")
                
        except KeyboardInterrupt:
            logging.info("Shutting down server...")
        except Exception as e:
            logging.error(f"Encountered an error: {e}")
        finally:
            if self.socket:
                self.socket.close()
                logging.info("Socket closed successfully")

def main():
    # Initialize and start the server
    server = TCPServer()
    server.run()

if __name__ == "__main__":
    main()
