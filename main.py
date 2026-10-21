#uvicorn main:app --reload

from app.exceptions import NoteNotFoundError
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Request
from app.routes.note_router import router as note_router

app = FastAPI()

@app.exception_handler(NoteNotFoundError)
async def note_not_found_handler(request: Request, exc: NoteNotFoundError):
    return JSONResponse(
        status_code=404,
        content={"detail": str(exc) or "Заметка не найдена"}
    )


app.include_router(router=note_router)