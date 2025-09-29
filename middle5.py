# coding=windows-1251 
# Обработка математических выражений
import re
def simply (string: str)->str:
    #print(string)
    pattern = re.compile(r'[\+\-\*\\]') #только знаки операций
    pattern2 = re.compile(r'\d+\.\d+|\d+') #только числа (целые или десятичные)
    pattern3 = re.compile(r'(?:\d+\.\d+|\d+) *[\+\-\*\\] *(?:\d+\.\d+|\d+)') #здесь объединено на выбор целое или десятичное, возможный пробел, один из знаков, возможный пробел, снова целое или десятичное
    pattern4 = re.compile(r'(\d+\.\d+|\d+) *([\+\-\*\\]) *(\d+\.\d+|\d+)') #с группировкой по числам и знакам в виде списков
    expressions = re.finditer(pattern4, string)
    result = re.sub(pattern4, calc, string)

    return result

def calc(matchobj):
    operator = matchobj.group(2)
    num1 = float(matchobj.group(1))
    num2 = float(matchobj.group(3))
    if(operator == "+"):
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2

    result = '{:.2f}'.format(round(result,2))
    return result

#text = input()
text = "10+0.01 равно 10.01, 0.127 округляется до 0.13"
#text = "10.4/2 0.13-2"
#text = "Текст без выражений"
#text = "Умножение 7*8 и деление 16/4"
#text = "0.5+0.5=1.0"
#text = "Смешанный текст 3.14*2 и 1.5/0.5"
#text = "10-5.5 и 2.75+3.25"
#text = "Сложение 0.1 + 0.2 и 0.3 - 0.1"
#text = "10.123 + 5.876 = 15.999"
print(simply(text))