coding=windows-1251

result = 0 + 1 and False * 2 | 3
print(0 + 1 and False * 2 | 3)

class C:
    def __init__(self,):
        self.x = []
        self.y = []
    def f(self, a, b):
        self.x.append(a)
        self.y.append(b)
    def g(self, a):
        for i in range(len(self.x)):
            if self.x[i] == a:
                return self.y[i]

myObject = C()
myObject.f(13,23)
print(myObject.g(13))

def can_apply(perfect_grades, age):
    if not perfect_grades:
        return 'poor grades'
    if age <= 5:
        return 'too young'
    if age <= 10:
        return 'elementary'
    if age <= 14:
        return 'middle'
    elif age <= 18:
        return 'high'
    return 'too old'

print(can_apply(False, 5))
print(can_apply(True, 14))

# ответ № 3

for i in range(0,10):
    if i % 2:
        continue
else:
    print(i, end='')

ответ № 2 -> 9

def a(): print('a')
def b(): print('b')
a+b

ответ № 1 операция сложения не определена для функций

def f(a, b=1, *c):
    s =0
    for i in c: s += 1
    s *= b
    s += a
    return a
print(f(1,2,1,2,b=2))

# ответ - сообщение об ошибке b

# ответ - zip()

class Matrix:
    def __init__(self, n):
        matrix = n*[n*[0]]
    def transpose(self):
        return [[row[i] for row in self.matrix] for i in range(len(self.matrix[0]))]

m = Matrix(2)
print(m)

# ответ - Атрибут неверно инициализирован

lst = [[i for i in range(j)] for j in [k for k in range(3)]]
print(lst)

# ответ № 1 -> 0, 0,1

with open('output.txt', 'w') as f:
    for i in range(1, 6):
        f.write(str(i) + '\n')

# ответ № 2

# ответ № 2 tkinter

import config;config.SETTINGS.debug=False # у SETTING нет атрибута debug
from config import SETTINGS;SETTINGS={'debug':False} # корректно меняет SETTINGS
from config import SETTINGS as cfg; cfg['debug'] = False # изменяет cfg['debug']
import config;config.SETTINGS={'debug':False} # изменяет config.SETTINGS
import config;config.SETTINGS['debug']=False # изменяет config.SETTINGS['debug']

print(config.SETTINGS['debug'])

ответ № 1 import config;config.SETTINGS.debug=False

import re
string = 'as32.4..Fh.d6kJ3.94asd'
pattern = r'.\.\D\d\w{2}'
print(re.findall(pattern, string))

# ответ # 5 h.d6kJ