# coding=windows-1251 
def check_candidates (names_input: str, scores_input: str)->str:
    names = names_input.split(',')
    scores = scores_input.split('|')
    sum = 0
    count = 0
    all_scores = []
    result = ""
    for lst in scores:
        sumOne = 0
        numverList = lst.split(',')
        for n in numverList:
            sum += int(n)
            sumOne += int(n)
            count += 1        
        all_scores.append(sumOne / len(numverList))
    average = sum / count
    for i in range(len(all_scores)):
        if(all_scores[i] > average and all_scores[i] > 50):
            result += names[i] + "\n"
    if(result==""): result="Никто"
    return result

#names_input = input()
#scores_input = input()
names_input = "Katrin,Marina,Vital,Ramin"
scores_input = "0,0,55,55|64,55,29,99|55,64,55,29|55,64,55,29"
# names_input = "Alex,Ivan"
# scores_input = "1,2,3,4|20,25,30,35"

result = check_candidates(names_input, scores_input)
print(result)