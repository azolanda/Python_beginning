import model
import view
import gui_phones


def book_begin():
    choose_view = view.enter_position(f'Выбрать отображение справочника:\n'
                                      f'1 - Консольное приложение\n'
                                      f'2 - Оконное приложение (GUI)\n')
    if choose_view == '1':
        choose_format = view.enter_position(f'Выбрать формат справочника:\n'
                                            f'1 - ФИО | Телефонный номер\n'
                                            f'2 - Телефонный номер | ФИО\n')
        while True:
            choose_operation = view.enter_position(f'Выбрать операцию:\n'
                                                   f'r - Показать справочник\n'
                                                   f'a - Добавить абонента\n'
                                                   f'f - Найти телефон/имя абонента \n'
                                                   f'd - Удалить абонента \n'
                                                   f'e - Выйти из программы \n')

            if choose_operation == 'a':
                model.init_name(view.enter_position('Ввести имя абонента'))
                model.init_tel(view.enter_position('Ввести телефон абонента'))
            if choose_operation == 'f':
                model.init_name(view.enter_position(
                    'Ввести имя абонента/телефон для поиска'))
            if choose_operation == 'd':
                model.init_name(view.enter_position(
                    'Ввести имя абонента/телефон для удаления'))
            if choose_operation == 'e':
                break

            result = model.operations[choose_operation](choose_format)

            view.print_result(result)
    elif choose_view == '2':
        app = gui_phones.PhonesApp()
        app.run()
    else:
        view.print_result(
            'Необходимо выбрать режим отображения справочника: ввести 1 или 2')
