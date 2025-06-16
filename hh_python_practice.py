def check_candidates (names_input: str, scores_input: str)->str:
    names = names_input.split(',')
    scores = scores_input.split('|')
    sum = 0
    count = 0
    for lst in scores:
        for n in lst.split(','):
            print(n)
            sum += int(n)
            count += 1
    
            
    print(f"sum={sum}")
    print(f"count={count}")
    average = sum / count            
    print(f"average={average}")


    

#names_input = input()
#scores_input = input()
names_input = "Katrin,Marina,Vital,Ramin"
scores_input = "0,0,55,55|64,55,29,99|55,64,55,29|55,64,55,29"
result = check_candidates(names_input, scores_input)
print(result)