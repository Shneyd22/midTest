import uuid
from datetime import date, datetime


class Note:
    def __init__(self, id, name, text, date):
        self.id = id
        self.name = name
        self.text = text
        self.date = date

    def getId(note):
        return note.id

    def getName(note):
        return note.name

    def getText(note):
        return note.text

    def getDate(note):
        return note.date

    def setId(note):
        note.id = id

    def setName(note, name):
        note.name = name

    def setText(note, text):
        note.text = text

    def setDate(note):
        note.date = date

    def toString(note):
        return note.id + ';' + note.name + ';' + note.text + ';' + note.date

    def info(note):
        return '\n Название: ' + note.name + '\n Содержание: ' + note.text + '\n Дата создания: ' + note.date
