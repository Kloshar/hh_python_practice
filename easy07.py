# coding=windows-1251
# ��������� �������
import re
def filter_vowels(text:str)->str:
    pattern = r'[���������]'
    newString = re.sub(pattern, '*', text, flags=re.IGNORECASE)    
    return newString

#text = input()
#text = "���� ���� ����"
text = "������,���!"
result = filter_vowels(text)
print(result)