import os

def create_storage():
    filename = "storage.txt"
    if os.path.exists(filename):
        print(f"Помилка: Файл '{filename}' уже існує")
    else:
        with open(filename, 'w', encoding="utf-8") as f:
            pass
        print(f"Файл '{filename}' створено")

def write_to_storage(text):
    with open("storage.txt", 'a', encoding="utf-8") as f:
        f.write(text + "\n")
    print("Текст додано")

def read_storage():
    try:
        with open("storage.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
            if not lines:
                print("Файл порожній.")
            else:
                print("\nВміст файлу:")
                for line in lines:
                    print(line.strip())
                print(" ")
    except FileNotFoundError:
        print("Помилка: Файл 'storage.txt' не знайдено")

def show_statistics():
    try:
        with open("storage.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
            total_lines = len(lines)
            non_empty_lines = 0
            for line in lines:
                if line.strip():
                    non_empty_lines += 1
            total_chars = 0
            for line in lines:
                total_chars += len(line.replace('\n', ''))
            print(f"\nСтатистика файлу:")
            print(f"1. Загальна кількість рядків: {total_lines}")
            print(f"2. Кількість непорожніх рядків: {non_empty_lines}")
            print(f"3. Кількість символів (без \\n): {total_chars}")
    except FileNotFoundError:
        print("Помилка: Неможливо порахувати статистику, файлу не існує")

def clear_storage():
    with open("storage.txt", 'w', encoding="utf-8") as f:
        pass
    print("Файл очищено")