# coding=windows-1251 
# ������� ���������
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

    #���������� ��� �������� ������
    for k in lst:
        lastSymbol = k[-1] #�������� ��������� ������
        if(lastSymbol == '='): beforeEqual = False

        #���� ����� ������ ���������
        if(beforeEqual):
            #���� � ����� x
            if(lastSymbol == variable):
                if(len(k) > 1):
                    variables.append(float(k.rstrip(lastSymbol))) #�� ��������� � ������ ����������
                else: variables.append(float(1))
            #���� � ����� �����
            elif(lastSymbol.isdigit() == True):
                numbers.append(-float(k)) #�� ��������� � ������ ����� � �������� ������
        
        #���� ����� ����� ���������
        else:
            #���� � ����� x
            if(lastSymbol == variable):
                variables.append(-float(k.rstrip(lastSymbol))) #�� ��������� � ������ ���������� � �������� ������
            #���� � ����� �����
            elif(lastSymbol.isdigit() == True):
                numbers.append(float(k)) #�� ��������� � ������ �����   

    leftSum = sum(variables)
    rightSum = sum(numbers)
    result = variable + " = " + str(round(rightSum / leftSum, 3))

    return result

#equation = input()
equation = "g + 2 = 5g - 10"
solution = solve_linear_equation(equation)
print(solution)