
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money = input("Введите сумму: ")

deposit=list(map(lambda x: x*float(money)/100, list(per_cent.values())))

print(list(map(int, deposit)))
print('Максимальная сумма, которую вы можете заработать — ', int(max(deposit)))
