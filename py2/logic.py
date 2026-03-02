def create_and_read_file():
    filename = "data.txt"
    text = """Joke 345
-How many tickles does it take to make an octopus laugh?
-Ten-tickles.

Анекдот 234
У двері постукали вісім раз...
Восьминіг подумав Штірліц"""

    # створюємо файл
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)

    # читаємо файл
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
        print("\nВміст файлу:\n")
        print(content)

def read_any_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
            print("\nВміст файлу:\n")
            print(content)
    except FileNotFoundError:
        print("Файл не знайдено!")