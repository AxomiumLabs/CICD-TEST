from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def test_funct():
    return {"messages":"Pm2 setup "}