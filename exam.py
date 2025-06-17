# coding=windows-1251
N = int(input())
numbers = []
i = 0
while(i<N):
    numbers.append(int(input()))
    i+=1
j=0
while(j<len(numbers)):    
    if(numbers[j]%4!=0): numbers.pop(j)
    j+=1
print(max(numbers))