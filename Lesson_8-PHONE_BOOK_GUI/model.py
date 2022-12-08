data_format = {'1': './Lesson_8-PHONE_BOOK_GUI/book_phones-first.txt',
               '2': './Lesson_8-PHONE_BOOK_GUI/book_phones-second.txt'}

name = 'empty_name'
tel = 'empty_tel'


def init_name(n):
    global name
    if n:
        name = n


def init_tel(t):
    global tel
    if t:
        tel = t


def init_book(format):
    with open(data_format[format], 'r') as phones:
        return [x[:-1].split(' | ') for x in phones.readlines()]


def read_book(format):
    return init_book(format)


def write_phone(format):
    person = ''
    if not (name == 'empty_name' or tel == 'empty_tel'):
        if format == '1':
            person = name + ' | ' + tel
        if format == '2':
            person = tel + ' | ' + name
        with open(data_format[format], 'a') as phones_first:
            phones_first.write(person + '\n')

        return 'Успешно записано: ' + person
    else:
        return 'Для добавления нового абонента необходимо ввести имя и телефон'


def find_person(format):
    telepone_book = init_book(format)
    filtered_book = list(
        filter(lambda x: name in x[0] or name in x[1], [i for i in telepone_book]))

    if len(filtered_book):
        return filtered_book
    else:
        return f'Справочник не содержит строк с "{name}"!'


def del_person(format):
    telepone_book = init_book(format)
    new_book = list(filter(lambda x: not (name in x[0] or name in x[1]), [
        i for i in telepone_book]))

    if not len(telepone_book) == len(new_book):
        person = ''

        with open(data_format[format], 'w') as phones_first:
            for i in new_book:
                person = i[0] + ' | ' + i[1]
                phones_first.write(person + '\n')

        return f'Успешно удалены строки справочника, содержащие "{name}"'
    else:
        return f'Справочник не содержит строк с "{name}"!'


operations = {'r': read_book, 'a': write_phone,
              'f': find_person, 'd': del_person}
