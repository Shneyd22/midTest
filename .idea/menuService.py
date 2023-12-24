import fileService
import Note
import noteService


def showAllNotes():
    array = fileService.readFile()
    for notes in array:
        print(Note.Note.info(notes))


def addNote():
    note = noteService.createNote()
    array = fileService.readFile()
    for notes in array:
        if Note.Note.getId(note) == Note.Note.getId(notes):
            Note.Note.setId(note)
    array.append(note)
    fileService.writeFile(array)
    print('Заметка успешно добавлена')


def deleteNote():
    id = input('Введите ID заметки, которую хотите удалить: ')
    array = fileService.readFile()
    for notes in array:
        if id == Note.Note.getId(notes):
            array.remove(notes)
            fileService.writeFile(array)
            print('Заметка успешно удалена')


def editNote():
    id = input('Выберите ID  заметки, которую Вы хотите перезаписать')
    array = fileService.readFile()
    l = True
    for notes in array:
        if id == Note.Note.getId(notes):
            l = False
            note = noteService.createNote()
            Note.Note.setName(notes, note.getName())
            Note.Note.setText(notes, note.getText())
            print('Изменения в заметке успешно сохранены')
    if l == True:
        print('Указанная заметка не найдена. Проверьте правильность внесенного ID!')
    fileService.writeFile(array)


def showNoteByDate():
    date = input('Введите дату и время создания заметки: ')
    array = fileService.readFile()
    l = True
    for notes in array:
        if date == Note.Note.getDate(notes):
            l = False
            print(Note.Note.info(notes))
    if l == True:
        print('Указанная заметка не найдена. Проверьте правильность введенной информации!')
