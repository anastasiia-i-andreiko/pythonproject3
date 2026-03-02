from logic import create_and_read_file, read_any_file

def main():
    while True:
        print("\nМеню:")
        print("1 - Створити файл з жартами і прочитати")
        print("2 - Прочитати будь-який файл")
        print("0 - Вийти")
        choice = input("Оберіть цифру (0-2): ")
        if choice == '1':
            create_and_read_file()
        elif choice == '2':
            filename = input("Введіть назву файлу: ")
            read_any_file(filename)
        elif choice == '0':
            print("Вихід.")
            break
        else:
            print("Помилка. Введіть цифру від 0 до 2.")
if __name__ == "__main__":
    main()