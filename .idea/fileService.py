import Note


def writeFile(array):
    file = open('notes.json', 'w', encoding='utf-8')
    file.seek(0)
    file.close()
    file = open('notes.json', 'w', encoding='utf-8')
    for notes in array:
        file.write(Note.Note.toString(notes))
        file.write('\n')
    file.close


def readFile():
    try:
        arrayNotes = []
        file = open('notes.json', 'r', encoding='utf-8')
        notes = file.read().strip().split('\n')
        file.close
        for n in notes:
            splitNote = n.split(';')
            note = Note.Note(
                id=splitNote[0], name=splitNote[1], text=splitNote[2], date=splitNote[3])
            arrayNotes.append(note)
    except Exception as err:
        print(Exception, err)
        print('Список сохраненных заметок пуст')
    finally:
        return arrayNotes
