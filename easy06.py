# coding=windows-1251
# �������
import re
def censor(text:str, blacklist:str)->str:
    newString = text
    badWords = blacklist.split(',')

    for b in badWords:
        replacer = '#' * len(b)
        pattern = r'\b' + b + r'\b'
        newString = re.sub(pattern, replacer, newString, flags=re.IGNORECASE)
    return newString

#text = input()
#blacklist = input()
#text = "��� ������� ������ �������!"
#blacklist = "�������"
#text = "���, ��-�� �������� �������� ������ ����� ������!"
#blacklist = "���,������"
text = "����� �� ���������� ��� �������� �������������, ������� �� ����������� ����������."
blacklist = "������,�����,��������"
censored_text = censor(text, blacklist)
print(censored_text)