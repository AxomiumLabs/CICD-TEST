from fastapi import FastAPI
import socket
from kubernetes import client, config

app = FastAPI()

# Load Kubernetes configuration from default location
config.load_kube_config()

@app.get("/")
def test_get():
    # Get hostname
    host_name = socket.gethostname()
    
    # Get replicas of pods
    v1 = client.CoreV1Api()
    pod_list = v1.list_namespaced_pod(namespace=host_name)
    num_replicas = len(pod_list.items)

    # Prepare response headers
    response_headers = {"X-Pod-Hostname": host_name}

    # Return response
    return {"message": "Hello EKS", "replicas": num_replicas}, 200, response_headers
