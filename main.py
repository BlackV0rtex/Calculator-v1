print("Калькулятор чисел!!")
#Пишем первое число
pervnum = int(input("Введите первое число: "))
#Пишем действие
act = input("Введите дейтвие (+,-,*,/): ")
#Пишем второе число
vtornum = int(input("Введите второе число: "))
#Проверям наличие плюса в act
if (act == "+"):
    #Если act = +, то делаем действие
    print(pervnum, act, vtornum, " = ", pervnum + vtornum)
#Проверям наличие минуса в act
elif (act == "-"):
    #Если act = -, то делаем действие
    print(pervnum, act, vtornum, " = ", pervnum - vtornum)
#Проверяем наличие умножения в act
elif (act == "*"):
    #Если act = *, то делаем действие
    print(pervnum, act, vtornum, " = ", pervnum * vtornum)
elif (act == "/"):
    #Проверяем на деление 0
    # Если вторнум = 0, то пишем ошибка
    # если не 0, то делаем Выч
        if (vtornum == 0):
            #Материм человека за ноль
            print("НА НОЛЬ ДЕЛИТЬ НЕЛЬЗЯ!!!!")
        else:
            print(pervnum, act, vtornum, " = ", pervnum / vtornum)
#Если ничего из предложенного нет то выдаётся это:
else:
    print("Такого действия нет")