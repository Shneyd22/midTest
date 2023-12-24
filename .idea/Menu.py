import menuService


def run():
    print('\n Приложение для работы с заметками.')
    command = ''
    while command != '6':
        command = input('\n Выберите нужную операцию: '
                        '\n 1 - вывод всех заметок из файла'
                        '\n 2 - добавление заметки'
                        '\n 3 - удаление заметки'
                        '\n 4 - редактирование заметки'
                        '\n 5 - открыть заметку по дате'
                        '\n 6 - выход\n')
        if command == '1':
            menuService.showAllNotes()
        elif command == '2':
            menuService.addNote()
        elif command == '3':
            menuService.deleteNote()
        elif command == '4':
            menuService.editNote()
        elif command == '5':
            menuService.showNoteByDate()
        elif command == '6':
            print('Работа приложения завершена')
            break
        else:
            print('Такой команды нет. Проверьте правильность ввода!')
