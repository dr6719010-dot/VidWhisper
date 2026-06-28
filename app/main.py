from fastapi import FastAPI

app = FastAPI(title="VidWhisper:")

@app.get("/", tags=["Home"])
def home():
    """Welcome Endpoint"""
    return {"message": "Welcome to VidWhisper"}