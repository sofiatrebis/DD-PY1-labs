def find_item_in_list(search_item, search_list):
    # итерируемся по списку, пока не найдем подходящий элемент
    for item_id, item in enumerate(search_list):
        if item == search_item:  # если нашли, то мы нашли его первое вхождение, возвращаем индекс
            return item_id
    return None  # нужный элемент не нашелся, возвращаем None


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_item_in_list(find_item, items_list)  # вызываем функцию для поиска индекса
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
