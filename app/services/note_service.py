from secrets import token_urlsafe
from app.exceptions import NoteNotFoundError
from app.redis_client import redis_client
from app.schemas import NoteCreate, NoteResponse, NoteDetail


def create_note(note: NoteCreate) -> NoteResponse:
    key = token_urlsafe(8)
    redis_key = f'note:{key}'

    time_to_live = note.ttl_seconds

    redis_client.set(redis_key, note.text, ex=time_to_live)

    return NoteResponse(key=key, ttl_seconds=time_to_live)


def get_note(key: str) -> NoteDetail:
    note = redis_client.get(f'note:{key}')
    if note is None:
        raise NoteNotFoundError('Нет такой заметки')
    time = redis_client.ttl(f'note:{key}')

    return NoteDetail(key=key, text=note, ttl_seconds=time)

def delete_note(key: str) -> int:
    succes_delete = redis_client.delete(f'note:{key}')

    if succes_delete == 0:
        raise NoteNotFoundError('Нет такой заметки')

    return succes_delete