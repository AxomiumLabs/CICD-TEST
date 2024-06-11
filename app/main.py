from fastapi import FastAPI
import socket

app = FastAPI()


@app.get("/")
def test_get():
    host_name=socket.gethostname()
    response_headers={"X-Pod-Hostname":host_name}
    return {"message":"Hello EKS new run ready"},200,response_headers