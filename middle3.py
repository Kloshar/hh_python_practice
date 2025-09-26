# coding=windows-1251
# Столярная мастерская
#from calendar import Day
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

    leftMinutes = daysList[0] #начальные минут первого дня

    i = 0
    while(i < len(ordersList)):
        #берём первую работу

        if leftMinutes >= ordersList[i]: #если минут в дне достаточно
            leftMinutes -= ordersList[i] #вычитаем минуты на выполнения заказа
            dates.append(count) #заводим номер дня для текущего заказа
            i += 1 #переходим к следующему заказу
            #print(dates)

        else: #если минут в дне осталось мало
            daysList.remove(daysList[0]) #выкидываем день
            if leftMinutes == daysList[0]: #если день полный, то копим минуты                
                leftMinutes += daysList[0] #добавляем минуты из следующего дня
            else:
                leftMinutes = daysList[0] #обновляем оставшиеся минуты
            count += 1    
    return ','.join(map(str, dates))

#timetable = input()
#orders = input()
# timetable = "9,11;10,10;7,14"
# orders = "1,60;5,30;10,10;2,32"
timetable = "10,15;11,13;10,15"
orders = "8,30;5,35;2,40"
# timetable = "6,10;7,12;8,14"
# orders = "3,40;2,60;1,45"
# timetable = "8,18;9,19;10,20"
# orders = "3,100;2,100;10,100" #здень неувязка - на заказ 1000 минут, но в часах работы есть максимум 600 минут

dates = schedule(timetable, orders)
print(dates)