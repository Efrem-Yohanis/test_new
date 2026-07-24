from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"name": "efrem", "age": 15, "message": "welcome to my FastAPI application!"}