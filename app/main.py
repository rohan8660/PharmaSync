from fastapi import FastAPI

app = FastAPI(title="PharmaSync", version="1.0.0")

@app.get("/")
def health_check():
    return {"status": "active", "system": "PharmaSync", "version": "v1"}