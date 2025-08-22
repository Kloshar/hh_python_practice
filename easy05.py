# coding=windows-1251
# Фильтрация результатов опроса
def filter_unique_words(answer_list:str)->str:
    allWords = answer_list.split()
    filtered = ""

    for w in allWords:
        if allWords.count(w) == 1:
            filtered += w + " "

    if(filtered == ""): filtered = "-1"

    return filtered.strip()

#answer_list = input()
answer_list = "python java c++ python"
#answer_list = "красный оранжевый жёлтый зелёный"
#answer_list = "ой ой ой"
unique_words = filter_unique_words(answer_list)
print(unique_words)