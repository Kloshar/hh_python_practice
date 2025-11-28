# coding=windows-1251 
# Рекурсивная сумма
def digital_root(n: int)-> int:    
    num = n
    amount = len(str(num))
    while amount > 1:        
        digits = list(str(num))
        num = 0
        for i in range(len(digits)):
            num += int(digits[i])
        amount = len(str(num))
    return num
input_string = input()
# input_string = 942
# input_string = 132189
# input_string = 3
# input_string = 760301
result = digital_root(int(input_string))
print(result)