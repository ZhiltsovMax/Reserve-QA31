
count = int(input("Введите количество билетов, которое хотите приобрести: "))

sum = 0
for i in range(count):
    age = int(input("Введите возраст %dго участника: " % (i+1)))
    if 18 <= age < 25:
        sum += 990
    elif age >= 25:
        sum += 1390
if count > 3:
    sum *= 0.9
print('Сумма к оплате: ', int(sum))
