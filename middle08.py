# coding=windows-1251 
# Анализ финансовых рынков
from turtle import reset
def get_dominate_prices(stock_prices: str)-> str:
    dominates = ""
    numbers = list(map(int,stock_prices.split()))
    for i in range(len(numbers)):
        result = not(any(numbers[i] < x for x in numbers[i+1:len(numbers)]))
        if result:    
            dominates += str(numbers[i]) + " "
    return dominates.strip()

stock_prices = input()
#stock_prices = "1 21 4 7 5"
#stock_prices = "1 21 34 45 5"

dominate_prices = get_dominate_prices(stock_prices)
print(dominate_prices)