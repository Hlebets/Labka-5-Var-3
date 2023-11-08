while True:
    main_input = input("Введіть назву тегу, який вам необхідний: ").lower()
    tagged_input = "#" + main_input
    file = open("text.txt", "r")

    try:
        with file:
            found_lines = [line for line in file if tagged_input in line.lower()]

        if found_lines:
            print("Знайдено наступні рядки: \n")
            for line in found_lines:
                print(line)
        elif main_input == "exit":
            break
        else:
            print("Такого тегу не існує")
    except:
        print("Помилка відкриття файлу")
