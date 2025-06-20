# coding=windows-1251
def mask(string_to_mask:str)->str:
    length = len(string_to_mask)
    newString = ""

    for i in range(0, length):
        if(i < length - 4): newString += "#"
        else: newString += string_to_mask[i]

    return newString
    
#string_to_mask = input()
string_to_mask = "JKMLkmlmcvlkjcvlkjJKJ512dfdL"

result = mask(string_to_mask)
print(result)