from fastapi import FastAPI
import socket

app = FastAPI()


@app.get("/")
def test_get():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 8000)
    try:
        # Connect to the server
        sock.connect(server_address)

        # Receive logs
        while True:
            data = sock.recv(1024)  # Adjust the buffer size as needed
            if not data:
                break
            print(data.decode())  # Assuming logs are encoded in UTF-8, adjust accordingly

    finally:
        # Close the socket connection
        sock.close()
    host_name=socket.gethostname()
    response_headers={"X-Pod-Hostname":host_name}
    return {"message":"Hello EKS scaled","data":data},200,response_headers