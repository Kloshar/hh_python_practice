# coding=windows-1251 
# ��������� �������������� ���������
import re
def simply (string: str)->str:
    #print(string)
    pattern = re.compile(r'[\+\-\*\\]') #������ ����� ��������
    pattern2 = re.compile(r'\d+\.\d+|\d+') #������ ����� (����� ��� ����������)
    pattern3 = re.compile(r'(?:\d+\.\d+|\d+) *[\+\-\*\\] *(?:\d+\.\d+|\d+)') #����� ���������� �� ����� ����� ��� ����������, ��������� ������, ���� �� ������, ��������� ������, ����� ����� ��� ����������
    pattern4 = re.compile(r'(\d+\.\d+|\d+) *([\+\-\*\\]) *(\d+\.\d+|\d+)') #� ������������ �� ������ � ������ � ���� �������
    #expressions = re.findall(pattern4, string)
    expressions = re.finditer(pattern4, string)

    print(calc(expressions)) 

    result = re.sub(pattern4, calc, string)

    return result

def calc(matchobj: list)->list:

    results = []

    #print(len(matchobj))

    for obj in matchobj:
        operator = obj[1]
        num1 = float(obj[0])
        num2 = float(obj[2])
        if(operator == "+"):
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2
        results.append(result)
    return results

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