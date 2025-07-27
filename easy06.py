# coding=windows-1251
def censor(text:str, blacklist:str)->str:
    allWords = answer_list.split()
    filtered = ""

    for w in allWords:
        if allWords.count(w) == 1:
            filtered += w + " "

    if(filtered == ""): filtered = "-1"

    return filtered.strip()

#text = input()
#blacklist = input()
text = "Это простой пример цензуры!"
blacklist = "цензуры"
censored_text = censor(text, blacklist)
print(censored_text)