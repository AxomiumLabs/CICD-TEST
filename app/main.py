from fastapi import FastAPI
import socket

app = FastAPI()


@app.get("/")
def test_get():
    host_name=socket.gethostname()
    domain=socket.getfqdn()
    response_headers={"X-Pod-Hostname":host_name}
    return {"message":"Hello EKS scaled"},200,response_headers