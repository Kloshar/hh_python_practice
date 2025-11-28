# coding=windows-1251 
# Экстремумы
def extreme_values(data: str, number_of_neighbors: int)-> str:
    result = ""
    nums = list(map(float, data.split(',')))
    r = iter(range(len(nums)))
    for i in r:
        if(i - number_of_neighbors >= 0 and i + number_of_neighbors < len(nums)): #отсекаем перевое и последнее значения
            near_numbers = nums[i-number_of_neighbors:i] + nums[i+1:i+1+number_of_neighbors] #получаем диапазон -2 и +2 числа
            if(all(nums[i] > x for x in near_numbers)):
                result += f"max: {nums[i]}, "
            if(all(nums[i] < x for x in near_numbers)):
                result += f"min: {nums[i]}, "
    if(result != ""):
        return result.rstrip(", ")
    else: return "Экстремумов не обнаружено"
'''
number_of_neighbors = input()
data = input()
number_of_neighbors = 1
data = "9.0,8.0,7.0,6.0,7.0,4.0,3.0,2.0,1.0"
number_of_neighbors = 1
data = "0.0,1.0,0.0,1.0,0.0,1.0,0.0"
number_of_neighbors = 1
data = "5.0,5.0,5.0,5.0"
number_of_neighbors = 2
data = "10.0,9.0,8.0,7.0,6.0,5.0"
number_of_neighbors = 2
data = "1,2,-5,4,5"
'''
number_of_neighbors = 1
data = "0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9"

extremes = extreme_values(data, number_of_neighbors)
print(extremes)