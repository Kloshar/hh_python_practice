# coding=windows-1251
# Дорогие товары
import re
def find_expencive_items(prices_string):
    prices =  prices_string.split(',')
    prices = list(map(float, prices))
    average = sum(prices) / len(prices)
    expencive = ""
    for i in prices:
        if(i > average):            
            expencive += f"{i:.2f}".rstrip('0').rstrip('.')
            expencive += '\n'
    expencive = expencive.rstrip('\n')
    if len(expencive) == 0: expencive = 'нет'
    return expencive

#prices_string = input()
#prices_string = "10,20,30,40,50"
prices_string = "10.5,20,15.75,30,25.5"
#prices_string = "5,5,5,5,5"

result = find_expencive_items(prices_string)
print(result)