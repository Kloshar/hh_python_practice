# coding=windows-1251 
# ��������� �������������� ���������
import re
from tokenize import String
def simply (string: str)->str:
    #print(string)
    pattern = re.compile(r'[\+\-\*\\]') #������ ����� ��������
    pattern2 = re.compile(r'\d+\.\d+|\d+') #������ ����� (����� ��� ����������)
    pattern3 = re.compile(r'(?:\d+\.\d+|\d+) *[\+\-\*\\] *(?:\d+\.\d+|\d+)') #����� ���������� �� ����� ����� ��� ����������, ��������� ������, ���� �� ������, ��������� ������, ����� ����� ��� ����������
    pattern4 = re.compile(r'(\d+\.\d+|\d+) *([\+\-\*\\]) *(\d+\.\d+|\d+)') #� ������������ �� ������ � ������ � ���� �������
    #result = re.findall(pattern4, string)

    result = re.findall(pattern4, string)     
    calc(result) 

    #result = re.sub(pattern4, calc, string)

    return ""

def calc(matchobj: list)->str:
    operator = matchobj[0][1]
    num1 = float(matchobj[0][0])
    num2 = float(matchobj[0][2])

    if(operator == "+"):        
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2        

    return result

#text = input()
#text = "10.01+0.01 \����� 10.01, 0.127 ����������� �� 0.13"
#text = "10.4/2 0.13-2"
#text = "����� ��� ���������"
#text = "��������� 7*8 � ������� 16/4"
#text = "0.5+0.5=1.0"
#text = "��������� ����� 3.14*2 � 1.5/0.5"
text = "10-5.5 � 2.75+3.25"
#text = "�������� 0.1 + 0.2 � 0.3 - 0.1"
#text = "10.123 + 5.876 = 15.999"
print(simply(text))