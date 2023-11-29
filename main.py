# from PyQt6.QtWidgets import QApplication, QMainWindow
# import sys
#
# class Window(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setGeometry(300, 300, 600, 400)
#         self.setWindowTitle("PyQt6 window")
#         self.show()
#
# app = QApplication(sys.argv)
# window = Window()
# sys.exit(app.exec())


# from kivy.app import App
# from kivy.uix.label import Label
#
# class MainApp(App):
#     def build(self):
#         label = Label(text='Hello from Kivy',
#                       size_hint=(.5,.5),
#                       pos_hint={'center_x':.5, 'center_y':.5})
#         return label
#
# if __name__ == '__main__':
#     app = MainApp()
#     app.run()

# from kivy.app import App
# from kivy.uix.image import Image
#
# class MainApp(App):
#     def build(self):
#         img = Image(source='Exemple.png',
#                     size_hint=(1, .5),
#                     pos_hint={'center_x':.5, 'center_y':.5}
#                     )
#         return img
#
# if __name__ == '__main__':
#     app = MainApp()
#     app.run()


# Отправка данных формы на сервер

# from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
# import requests
#
#
# # Функция для отправки данных формы на сервер
# def send_form_data():
# url = "https://api.example.com/submit" # Замените на URL вашего сервера
# payload = {"name": name_input.text(), "email": email_input.text()}
# response = requests.post(url, data=payload)
# if response.status_code == 200:
# message_label.setText("Данные успешно отправлены")
# else:
# message_label.setText("Ошибка при отправке данных")
#
#
# # Создать приложение
# app = QApplication([])
#
# # Создать основное окно
# window = QMainWindow()
# window.setWindowTitle("Отправка формы на сервер")
#
# # Создать виджет
# widget = QWidget()
# layout = QVBoxLayout()
#
# # Создать поля ввода
# name_label = QLabel("Имя:")
# layout.addWidget(name_label)
# name_input = QLineEdit()
# layout.addWidget(name_input)
#
# email_label = QLabel("Email:")
# layout.addWidget(email_label)
# email_input = QLineEdit()
# layout.addWidget(email_input)
#
# # Создать кнопку отправки данных формы
# submit_button = QPushButton("Отправить")
# submit_button.clicked.connect(send_form_data)
# layout.addWidget(submit_button)
#
# # Создать метку для вывода сообщений
# message_label = QLabel()
# layout.addWidget(message_label)
#
# # Установить layout для виджета
# widget.setLayout(layout)
#
# # Установить виджет в основное окно
# window.setCentralWidget(widget)
#
# # Показать основное окно
# window.show()
#
# # Запустить приложение
# app.exec()


# import kivy
# import random
#
# from kivy.app import App
# from kivy.uix.button import Button
# from kivy.uix.boxlayout import BoxLayout
#
# red = [1,0,0,1]
# green = [0,1,0,1]
# blue = [0,0,1,1]
# purple = [1,0,1,1]
#
# class HBoxLayoutExample(App):
#     def build(self):
#         layout = BoxLayout(padding=10)
#         colors = [red, green, blue, purple]
#
#         for i in range(5):
#             btn = Button(text="Button #%s" % (i+1),
#                          background_color=random.choice(colors))
#
#             layout.add_widget(btn)
#
#         return layout
#
# if __name__ == "__main__":
#     app = HBoxLayoutExample()
#     app.run()




#Разработайте графическое приложение с использованием выбранной графической библиотеки,
# которое позволяет пользователю создавать, сохранять и открывать файлы

# from kivy.app import App
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.button import Button
# from kivy.uix.label import Label
# from kivy.uix.textinput import TextInput
#
#
# class MyApp(App):
#
#     def __init__(self):
#
#         super().__init__()
#
#         self.label = Label(text='')
#         self.input_data = TextInput(hint_text='Введите название файла')
#         self.input_data2 = TextInput(hint_text='Введите текст для файла')
#         self.button = Button(text='Открыть файл')
#         self.button_2 = Button(text='Создать файл')
#         self.button_3 = Button(text='Записать в файл')
#
#         self.button.bind(on_press=self.open_file)
#         self.button_2.bind(on_press=self.create_file)
#         self.button_3.bind(on_press=self.write_file)
#
#     def build(self):
#         layout = BoxLayout(orientation='vertical')
#         layout.add_widget(self.input_data)
#         layout.add_widget(self.input_data2)
#         layout.add_widget(self.button)
#         layout.add_widget(self.button_2)
#         layout.add_widget(self.button_3)
#         layout.add_widget(self.label)
#         return layout
#
#     def open_file(self, *args):
#         name = self.input_data.text
#         try:
#             with open(name, 'r') as f:
#                 content = f.read()
#                 if content:
#                     self.label.text = content
#                 else:
#                     self.label.text = "Файл пуст"
#         except FileNotFoundError:
#             self.label.text = "Такого файла нет"
#
#
#
#     def create_file(self, *args):
#         name = self.input_data.text
#         try:
#             with open(name, 'w') as f:
#                 self.label.text = f"Файл '{name}' создан"
#         except Exception as e:
#             self.label.text = "Ошибка: " + str(e)
#
#
#     def write_file(self, *args):
#         name = self.input_data.text
#         text = self.input_data2.text
#         try:
#             with open(name, 'a') as f:
#                 f.write(text + "\n")
#                 self.label.text = "Текст записан в файл"
#         except FileNotFoundError:
#             self.label.text = "Такого файла нет"
#
#
# if __name__ == '__main__':
#     MyApp().run()
