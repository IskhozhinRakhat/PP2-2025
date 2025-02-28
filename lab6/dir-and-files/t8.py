import os

path = "C:\Users\Рахат\Desktop\PP2-2025\task 8.txt"

if not os.path.exists(path):
    print(f"Ошибка: файл по пути '{path}' не существует")

if not os.access(path, os.W_OK):
    print(f"Ошибка: нет прав на удаление файла '{path}'")
        
os.remove(path)