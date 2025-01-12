# импортируем необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    data = []  # массив с данными

    # Открытие файла для получения чтения словарей из сsv строк
    with open(INPUT_FILENAME, "r") as file:
        # вычитываем данные из csv.DictReader
        for row in csv.DictReader(file):
            data.append(row)

    # Сериализуем в файл с отступами равными 4
    with open(OUTPUT_FILENAME, "w") as file:
        json.dump(data, file, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")



