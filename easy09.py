# coding=windows-1251
# Система оценивания
def passing_scores(scores:str)->str:
    scores = scores.split(' ')
    passed = 0
    not_passed = 0

    for i in scores:
        if(int(i) >= 60): passed += 1
        else: not_passed += 1

    return f"Прошли {passed}, не прошли {not_passed}"
    
#scores = input()
scores = "78 91 0 12 66 32"
result = passing_scores(scores)
print(result)