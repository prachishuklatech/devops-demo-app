from fastapi import FastAPI
from datetime import datetime, timezone
import os

app = FastAPI(
    title="DevOps Demo Application",
    description="A portfolio project demonstrating Docker, Kubernetes, Jenkins and ArgoCD",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "application": "DevOps Demo Application",
        "message": "Welcome to our DevOps Portfolio Project!",
        "version": "1.0.0",
        "environment": os.getenv("APP_ENV", "development"),
        "status": "running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

@app.get("/info")
def info():
    return {
        "application": "DevOps Demo Application",
        "environment": os.getenv("APP_ENV", "development"),
        "hostname": os.getenv("HOSTNAME", "local"),
        "platform": "Docker + Kubernetes"
    }
