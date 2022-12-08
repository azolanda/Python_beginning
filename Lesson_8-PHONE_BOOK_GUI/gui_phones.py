from kivy.app import App
from kivy.properties import ObjectProperty

from kivy.uix.boxlayout import BoxLayout

from kivy.uix.label import Label

import model


class PhonesContainer(BoxLayout):
    grid_phones = ObjectProperty()
    find_name = ObjectProperty()
    enter_name = ObjectProperty()
    enter_tel = ObjectProperty()
    result_label = ObjectProperty()

    def kv_init_book(self):
        self.result_label.text = 'Здесь появится сообщение о результате операции'
        gp = self.grid_phones
        gp.clear_widgets()
        book = model.read_book('1')
        gp.rows = len(book)

        for i in range(0, gp.rows):
            self.label = Label(
                text=book[i][0], halign="left", valign="middle", color="#333233")
            self.label.bind(size=self.label.setter('text_size'))

            gp.add_widget(self.label)
            gp.add_widget(Label(text=book[i][1], color="#333233"))

    def __init__(self, **kwargs):
        super(PhonesContainer, self).__init__(**kwargs)
        self.kv_init_book()

    def kv_init_name(self):
        model.init_name(self.find_name.text)

    def kv_enter_name(self):
        model.init_name(self.enter_name.text)

    def kv_enter_tel(self):
        model.init_tel(self.enter_tel.text)

    def kv_add_abonent(self):
        self.kv_enter_name()
        self.kv_enter_tel()
        result = model.operations['a']('1')
        self.enter_name.text = ''
        self.enter_tel.text = ''
        model.init_name('empty_name')
        model.init_tel('empty_tel')
        self.kv_init_book()
        self.result_label.text = ''
        self.result_label.text = result

    def kv_find(self):
        self.kv_init_name()
        gp = self.grid_phones
        gp.clear_widgets()
        result = model.operations['f']('1')
        if type(result) is list:
            gp.rows = len(result)

            for i in range(0, gp.rows):
                self.label = Label(
                    text=result[i][0], halign="left", valign="middle", color="#333233")
                self.label.bind(size=self.label.setter('text_size'))

                gp.add_widget(self.label)
                gp.add_widget(
                    Label(text=result[i][1], color="#333233"))
            self.result_label.text = f'Запрос на поиск выполнен успешно'
        else:
            self.result_label.text = result

        self.find_name.text = ''
        model.init_name('empty_name')

    def kv_del(self):
        self.kv_init_name()
        result = model.operations['d']('1')
        self.find_name.text = ''
        model.init_name('empty_name')
        self.kv_init_book()
        self.result_label.text = result


class PhonesApp(App):
    def build(self):
        self.title = 'Телефонный справочник'
        return PhonesContainer()
