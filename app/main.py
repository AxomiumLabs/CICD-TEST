from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def test_funct():
    return {"messages":"EKS setup new run "}