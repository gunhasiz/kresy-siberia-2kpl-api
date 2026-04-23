from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.endpoints import status

app = FastAPI(
    title="Recon API",
    description="API for managing Kresy-Siberia reconnaissance data",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(status.router, prefix="/status", tags=["status"])

@app.get("/", tags=["health"])
def read_root() -> dict[str, str]:
    """
    Health check endpoint to verify the API is running.
    """
    return {
        "status": "ok", 
        "message": "Recon API is up and running!"
    }