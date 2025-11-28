# coding=windows-1251 
# Конвертация римских чисел

def roman_to_decimal(roman_number: str)-> str:
    sum = 0
    r = iter(range(len(roman_number)))
    for i in r:
        if(i != len(roman_number) - 1): 
            if roman_numerals[roman_number[i]] < roman_numerals[roman_number[i + 1]]:
                sum += roman_numerals[roman_number[i+1]] - roman_numerals[roman_number[i]]
                next(r)
            else:
                sum += roman_numerals[roman_number[i]]
        else: sum += roman_numerals[roman_number[i]]
    return sum
roman_numerals = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}

#roman_number = input()
roman_number = "MCMXCIV"
roman_number = "XLII"
roman_number = "CDXLIV"
roman_number = "MMXX"
roman_number = "DCCCXLV"
roman_number = "CCLXXXI"
roman_number = "MCCXXXIV"

decimal_number = roman_to_decimal(roman_number)
print(decimal_number)