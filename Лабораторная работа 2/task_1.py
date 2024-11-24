money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

count = 0  # количество  месяцев, которое можно протянуть без долгов
while money_capital + salary - spend > 0:  # пока можем прожить еще месяц без долга
    money_capital = money_capital + salary - spend  # обновляем баланс
    spend = spend * (1 + increase)  # spend растет ежемесячно
    count += 1  # прошел месяц, обновляем ответ

print("Количество месяцев, которое можно протянуть без долгов:", count)
