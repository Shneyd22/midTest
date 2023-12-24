import Note
import uuid
from datetime import datetime


def createNote():
    id = str(uuid.uuid1())
    name = input('Введите название заметки: ')
    text = input('Введите содержание заметки: ')
    date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
    return Note.Note(id = id, name = name, text = text, date = date)
