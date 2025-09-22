# coding=windows-1251
# Обработка гласных
import re
def filter_vowels(text:str)->str:
    pattern = r'[ауоиэыяюеё]'
    newString = re.sub(pattern, '*', text, flags=re.IGNORECASE)    
    return newString

#text = input()
#text = "Мама мыла раму"
text = "Привет,мир!"
result = filter_vowels(text)
print(result)