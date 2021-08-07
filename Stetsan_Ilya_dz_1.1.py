# Вводим количество секунд
while True:
    duration = int(input("Введите продолжительность в секундах: "))
    if duration >= 1 and duration <= 59:
        print(duration, "сек")
    elif duration >= 60 and duration <= 120:
        print(duration // 60, "мин", duration % 60, "сек")
    elif duration > 120 and duration < 3600:
         print(duration // 60, "мин", duration % 60, "сек")
    elif duration >= 3600 and duration <= 86400:
        print(duration // 3600, "час", (duration // 60) % 60, "мин", duration % 60, "сек")
    elif duration >= 86400:
        print (duration//86400, "дн",(duration % 86400) // 3600, "час", (duration // 60) % 60, "мин", duration % 60, "сек")
    elif duration < 1:
        print("Введите число от 1 и больше.")
    else:
        print("Вы ввели неверные данные, попробуйте еще раз.")









