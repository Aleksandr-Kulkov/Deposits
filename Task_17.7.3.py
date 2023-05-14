per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input("Введите сумму вклада: "))
deposit = [int(i * money / 100) for i in per_cent.values()]
print("Накопленные средства за год вклада в каждом из банков: ", deposit)
print("Максимальная сумма, которую вы можете заработать — ", max(deposit))