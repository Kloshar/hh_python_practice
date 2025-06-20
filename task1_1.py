# coding=windows-1251
def vowel_percentage(slogan:str)->str:
    vowels = "����������Ũ�������"
    consonant = "�����������������������"
    inputString = slogan.replace(' ','')
    amountVowels = 0
    amountConsonant = 0

    for ch in inputString:
        for cha in consonant:
            if ch.lower() == cha: amountConsonant += 1

    for ch in inputString:
        for cha in vowels:
            if ch == cha: amountVowels += 1

    percent = str(round (amountVowels * 100 / (amountVowels + amountConsonant))) + '%'

    return percent

#slogan = input()
slogan = "����� ������� ������� � ���� �����������?"
percentage = vowel_percentage(slogan)
print(percentage)