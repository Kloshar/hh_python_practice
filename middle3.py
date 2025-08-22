# coding=windows-1251
# Столярная мастерская
import math

def schedule(timetable: str, orders: str)->str:
    ordersList = []
    daysList = []
    dates = []
    count = 0

    for i in orders.split(';'):
        ordersList.append(math.prod(map(int,i.split(','))))

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

        if(leftMinutes > 0):
            dates.append(count)
        else:
            daysList.pop(0)
            count += 1
            i -= 1
            leftMinutes = daysList[0]
            print(f"Выкинули день, теперь leftMinutes = {leftMinutes}")
        i += 1
    
    return ', '.join(map(str, dates))

#timetable = input()
#orders = input()
timetable = "9,11;10,10;7,14"
orders = "1,60;5,30;10,10;2,32"
dates = schedule(timetable, orders)
print(dates)