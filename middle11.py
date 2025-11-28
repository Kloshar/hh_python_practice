# coding=windows-1251 
# Список для чтения
# Совершенно очевидно, что задание не доделано. Нет создания экземпляров класса и вызова методов класса, нет возвращаемых значений
# поэтому добавлен дополнительный код на моё усмотрение

class Student:
    def __init__(self,name,interests):
        self.name = name
        self.interests = interests

class Library:
    def __init__(self):
        pass
    def compile_list(self,student):
        pass

def CreateBookLists(data:str)->str:    
    students = [] # список студентов и увлечений
    for s in data.split('\n')[0].split(';'): # разделяем строку на студентов
        part = s.split(':')
        students.append(Student(part[0], part[1])) # добавляем студентов и увлечения в список
    
    books = dict() # словарь кник и их разделов
    for o in data.split('\n')[1].split(';'): # делим список на отдельные книги
        book = o.split(':')
        books[book[0]] = book[1] # добавляем книгу в словарь   
     


'''
student_data = input()
'''

student_data = "Светлана:Химия;Игорь:Математика,Физика\nХимия для чайников:Химия;Математика для всех:Математика;Квантовая механика:Физика"
result = CreateBookLists(student_data)
#print(result)