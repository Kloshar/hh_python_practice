# coding=windows-1251 
def check_candidates (names_input: str, scores_input: str)->str:
    names = names_input.split(',')
    scores = scores_input.split('|')
    sum = 0
    count = 0
    all_scores = []
    for lst in scores:
        sumOne = 0
        for n in lst.split(','):
            print(n)
            sum += int(n)
            sumOne += int(n)
            count += 1
        print(f"Длина списка: {len(lst)}")
        all_scores.append(sumOne / len(lst))
    average = sum / count

    print(f"all_scores={all_scores}")
    

#names_input = input()
#scores_input = input()
names_input = "Katrin,Marina,Vital,Ramin"
scores_input = "0,0,55,55|64,55,29,99|55,64,55,29|55,64,55,29"
result = check_candidates(names_input, scores_input)
print(result)