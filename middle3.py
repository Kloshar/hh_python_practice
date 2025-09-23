# coding=windows-1251
# Столярная мастерская
import math

def schedule(timetable: str, orders: str)->str:
    ordersList = []
    daysList = []
    dates = []
    count = 0

    for i in orders.split(';'):
        mitutesForOrder = math.prod(map(int,i.split(',')))
        ordersList.append(mitutesForOrder)

    for i in timetable.split(';'):
        hours = list(map(int,i.split(',')))
        minutes = (hours[1] - hours[0])*60
        daysList.append(minutes)

    leftMinutes = daysList[0]
    print(f"Начальные минуты из первого дня = {leftMinutes}")

    i = 0
    while(i < len(ordersList)):
        print(f"i={i}")

        leftMinutes = leftMinutes - ordersList[i]
        print(f"leftMinutes = {leftMinutes}")

        if(leftMinutes >= 0): #если минуты остались, то записываем текущий день как дату выполнения заказа
            dates.append(count)
        elif(ordersList[i] > 600 & daysList[0] >= 600): #если минут не осталось и заказ на 600 минут
            print(f"ordersList[i] = {ordersList[i]}, daysList.count =  {len(daysList)}, daysList[0] = {daysList[0]}, dates = {dates}, count = {count}")
            count += 1 #прибавляем затраченный день
            i -= 1 
            leftMinutes = daysList[0] #так как день из списка не удалил, то и оставшиеся минуты не изменились
        else:
            daysList.pop(0)
            count += 1
            i -= 1
            leftMinutes = daysList[0] #индекс за пределами массива
            print(f"Выкинули день, теперь leftMinutes = {leftMinutes}")
        i += 1
    
    return ','.join(map(str, dates))

#timetable = input()
#orders = input()
# timetable = "9,11;10,10;7,14"
# orders = "1,60;5,30;10,10;2,32"
# timetable = "6,10;7,12;8,14"
# orders = "3,40;2,60;1,45"
timetable = "8,18;9,19;10,20"
orders = "3,100;2,100;10,100" #здень неувязка - на заказ 1000 минут, но в часах работы есть максимум 600 минут

dates = schedule(timetable, orders)
print(dates)