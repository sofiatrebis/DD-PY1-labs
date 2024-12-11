def get_participants_set(group, sep=","):  # функция для получения множества участников из строки и разделителя
    return set(group.split(sep=sep))


def find_common_participants(first_group, second_group, sep=","):
    # получаем множества участников из обоих строк
    first_group_set = get_participants_set(first_group, sep)
    second_group_set = get_participants_set(second_group, sep)
    return sorted(first_group_set.intersection(second_group_set))  # пересекаем множества и сортируем результат


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# получаем общих участников
common_participants = find_common_participants(participants_first_group, participants_second_group)

for participant in common_participants:
    print(participant)  # выводим общих участников
