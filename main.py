from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"name": "efrem tes efrem yohanis new test", "age": 15}