from py1.logic import *

def main():
    while True:
        print("\n1 - Створити файл\n"
              "2 - Записати текст у файл\n"
              "3 - Прочитати файл\n"
              "4 - Порахувати статистику\n"
              "5 - Очистити файл\n"
              "0 - Вийти\n")

        choice = input("Оберіть цифру (0-5): ")

        if choice == '1':
            create_storage()
        elif choice == '2':
            text = input("Введіть текст: ")
            write_to_storage(text)
        elif choice == '3':
            read_storage()
        elif choice == '4':
            show_statistics()
        elif choice == '5':
            clear_storage()
        elif choice == '0':
            print("Вихід.")
            break
        else:
            print("Помилка. Введіть цифру від 0 до 5.")

if __name__ == "__main__":
    main()

