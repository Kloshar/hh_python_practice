# coding=windows-1251
# Цензура
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
#text = "Это простой пример цензуры!"
#blacklist = "цензуры"
#text = "Кот, из-за которого пришлось купить новую посуду!"
#blacklist = "кот,посуду"
text = "Книга не показалась ему особенно занимательной, модерну он предпочитал постмодерн."
blacklist = "модерн,книга,особенно"
censored_text = censor(text, blacklist)
print(censored_text)