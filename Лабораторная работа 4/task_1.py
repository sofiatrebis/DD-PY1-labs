import json


def task() -> float:
    # открываем файл и считываем данные
    data = []
    with open("input.json") as file:
        data = json.load(file)

    # проходим по всем элементам
    result = 0
    for item in data:
        result += item['score'] * item['weight']  # обновляем ответ

    # возвращаем округленный ответ
    return round(result, 3)


print(task())
