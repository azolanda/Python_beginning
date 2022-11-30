import model
import view


def book_begin():
    choose_format = view.enter_position(f'Выбрать формат справочника:\n'
                                        f'1 - ФИО | Телефонный номер\n'
                                        f'2 - Телефонный номер | ФИО\n')

    choose_operation = view.enter_position(f'Выбрать операцию:\n'
                                           f'r - Показать справочник\n'
                                           f'a - Добавить абонента\n'
                                           f'f - Найти телефон/имя абонента \n'
                                           f'd - Удалить абонента \n')

    if choose_operation == 'a':
        model.init_name(view.enter_position('Ввести имя абонента'))
        model.init_tel(view.enter_position('Ввести телефон абонента'))
    if choose_operation == 'f':
        model.init_name(view.enter_position(
            'Ввести имя абонента/телефон для поиска'))
    if choose_operation == 'd':
        model.init_name(view.enter_position(
            'Ввести имя абонента/телефон для удаления'))

    result = model.operations[choose_operation](choose_format)

    view.print_result(result)
