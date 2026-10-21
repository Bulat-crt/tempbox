from fastapi import APIRouter, HTTPException
from app.schemas import NoteResponse, NoteCreate, NoteDetail
from app.exceptions import NoteNotFoundError
from app.services.note_service import create_note, get_note, delete_note

router = APIRouter()

@router.post('/notes', response_model=NoteResponse, status_code=201)
def add_note(note: NoteCreate):
    new_note = create_note(note)

    return new_note

@router.get('/notes/{key}', response_model=NoteDetail)
def get_note_by_key(key: str):
    try:
       note = get_note(key)
    except NoteNotFoundError:
        raise HTTPException(
            status_code=404,
            detail='Нет такой заметки'
        )

    return note

@router.delete('/notes/{key}', status_code=204)
def delete_note_by_key(key: str):
    try:
        delete_note(key)
    except NoteNotFoundError:
        raise HTTPException(
            status_code=404,
            detail='Нет такой записи'
        )

    return True