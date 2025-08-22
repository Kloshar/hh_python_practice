# coding=windows-1251 
# Решение уравнений
from os import replace

def solve_linear_equation (equation: str)->str:
    variable = ''
    for i in equation:
        if(i.isalpha() == True):
            variable = i    

    equation = equation.replace('- ', '-')
    lst = equation.split(' ')
    variables = []
    numbers = []

    beforeEqual = True

    #перебираем все элементы списка
    for k in lst:
        lastSymbol = k[-1] #забираем последний символ
        if(lastSymbol == '='): beforeEqual = False

        #если перед знаком равенства
        if(beforeEqual):
            #если в конце x
            if(lastSymbol == variable):
                if(len(k) > 1):
                    variables.append(float(k.rstrip(lastSymbol))) #то добавляем в список переменных
                else: variables.append(float(1))
            #если в конце цифра
            elif(lastSymbol.isdigit() == True):
                numbers.append(-float(k)) #то добавляем в список чисел с обратным знаком
        
        #если после знака равенства
        else:
            #если в конце x
            if(lastSymbol == variable):
                variables.append(-float(k.rstrip(lastSymbol))) #то добавляем в список переменных с обратным знаком
            #если в конце цифра
            elif(lastSymbol.isdigit() == True):
                numbers.append(float(k)) #то добавляем в список чисел   

    leftSum = sum(variables)
    rightSum = sum(numbers)
    result = variable + " = " + str(round(rightSum / leftSum, 3))

    return result

#equation = input()
equation = "g + 2 = 5g - 10"
solution = solve_linear_equation(equation)
print(solution)