from fastapi import FastAPI

app = FastAPI(title="FastAPI + MySQL")

@app.get("/health")
def health_check():
    return {"status": "ok"}
