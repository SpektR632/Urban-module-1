import os
from datetime import datetime
for root, dirs, files in os.walk(r'C:\Users\Роман\PycharmProjects\pythonUrbanUniversity\Module 7'):
    print(files)
    for file in files:
        filepath = os.path.dirname(__file__)
        formatted_time = datetime.fromtimestamp(os.path.getmtime(file)).strftime('%d.%m.%Y %H:%M')
        file_size = os.path.getsize(file)
        parent_dir = os.path.dirname(__file__[os.path.dirname(__file__).rfind("\\")+1:])

        print(f"Обнаружен файл: {file}, Путь: {filepath}, Размер: {file_size} байт, Время изменения: {formatted_time},"
              f" Родительская директория: {parent_dir}")
