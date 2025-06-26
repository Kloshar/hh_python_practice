# coding=windows-1251
# result = 0 + 1 and False * 2 | 3
# print(0 + 1 and False * 2 | 3)

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