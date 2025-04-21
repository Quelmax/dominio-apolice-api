# app/main.py

from fastapi import FastAPI
from app.api.rota_apolice import rota as apolices_router

app = FastAPI(
    title="API de Apólices de Seguro",
    version="1.0.0"
)

app.include_router(apolices_router, prefix="/api/v1")
