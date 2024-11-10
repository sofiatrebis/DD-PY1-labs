size = 1.44  # объем дискеты в Мб
pages = 100  # количество страниц в книге
lines = 50  # количество строк на странице
symbols = 25  # количество символов в строке
bytes_per_symbol = 4  # количество байт в одном символе

size_in_bytes = size * 1024 * 1024  # размер дискеты в байтах
bytes_per_book = pages * lines * symbols * bytes_per_symbol  # количество байт в книге

count = round(size_in_bytes / bytes_per_book)  # количество целых книг, помещающихся на дискету
print("Количество книг, помещающихся на дискету:", count)
