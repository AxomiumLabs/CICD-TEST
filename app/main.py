from fastapi import FastAPI
import socket
from kubernetes import client, config
from kubernetes.client.rest import ApiException

app = FastAPI()

# Initialize Kubernetes client
try:
    config.load_incluster_config()  # Use this when running inside a Kubernetes cluster
except config.ConfigException:
    config.load_kube_config()  # Use this for local development/testing with a kubeconfig file

@app.get("/")
def test_get():
    host_name = socket.gethostname()
    
    # Initialize response headers with hostname
    response_headers = {"X-Pod-Hostname": host_name}
    
    try:
        # Get the current namespace
        namespace = open('/var/run/secrets/kubernetes.io/serviceaccount/namespace').read()
        
        # Create API instance
        v1 = client.CoreV1Api()
        
        # List all pods in the current namespace
        pods = v1.list_namespaced_pod(namespace)
        
        # Count the number of pods
        pod_count = len(pods.items)
        
        # Add pod count to response headers
        response_headers["X-Total-Pods"] = str(pod_count)
    except ApiException as e:
        print("Exception when calling CoreV1Api->list_namespaced_pod: %s\n" % e)
        response_headers["X-Total-Pods"] = "Error"
    
    return {"message": "Hello EKS"}, 200, response_headers
