salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

total_salary = salary * months  # Суммарный заработок за month месяцев
total_spend = 0  # Суммарные траты за month месяцев
for i in range(months):
    total_spend += spend  # Каждый месяц тратим spend
    spend *= 1 + increase  # spend растет ежемесячно

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(total_spend - total_salary))
