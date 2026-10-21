#uvicorn main:app --reload

from fastapi import FastAPI
from app.routes.note_router import router as note_router

app = FastAPI()

app.include_router(router=note_router)