# coding=windows-1251
# N = int(input())
# numbers = []
# i = 0
# while(i<N):
#     numbers.append(int(input()))
#     i+=1
# j=0
# while(j<len(numbers)):    
#     if(numbers[j]%4!=0): numbers.pop(j)
#     j+=1
# print(max(numbers))

# result = 0 + 1 and False * 2 | 3

# result = [1]
# result.append((0, 1))
# result += (0, 1)

# weight = 10
# result = (0 if weight < 70 else 1) if weight > 30 else -1

# for i in range(0, 10):    
#     if i % 2:        
#         continue
#     else:    
#         print(i, end='')

# a = 1
# def g():    
#     print(a)    
#     a += 1    
#     print(a)
# def f():    
#     print(a)    
#     a += 1    
#     g()    
#     print(a)
# f()

# class Clock:    
#     def __init__(self, type_of_clock):        
#         self.type = type_of_clock        
#         self.__time = "00:00:00"        
#     def set_time(time):        
#         self.__time = time    
#     def tell_time():        
#         return self.__time

result = [i for i in range(5,26) if abs(i**0.5)**2 == i]

print(result)