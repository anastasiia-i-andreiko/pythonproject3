def copy_file_multiple(original, copies):
    try:
        with open(original, "rb") as f:
            data = f.read()
        for i in range(1, copies + 1):
            copy_name = original.split(".")[0] + f"_copy{i}." + original.split(".")[1]
            with open(copy_name, "wb") as f_copy:
                f_copy.write(data)
            print(f"Створено: {copy_name}")
    except FileNotFoundError:
        print(f"Файл '{original}' не знайдено")


def main():
    num_copies = int(input("Скільки копій робити?: "))

    copy_file_multiple("task3.gif", num_copies)
    copy_file_multiple("task3_2.jpg", num_copies)


if __name__ == "__main__":
    main()