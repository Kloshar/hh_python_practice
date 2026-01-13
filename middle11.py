# coding=windows-1251 
# Список для чтения
# Совершенно очевидно, что задание не доделано. Нет создания экземпляров класса и вызова методов класса, нет возвращаемых значений
# поэтому добавлен дополнительный код на моё усмотрение
# переделал код чтобы стало больше похоже на задание, но некоторые методы пришлось изменить

class Student:
    def __init__(self,name,interests):
        self.name = name
        self.interests = interests.split(',')

class Library:
    def __init__(self,book_data:str):
        self.books = dict()
        for o in book_data.split(';'): # делим список на отдельные книги
            book = o.split(':')
            self.books[book[0]] = book[1] # добавляем книгу в словарь
    def compile_list(self,student_data:str)->str:
        students = [] # список студентов и увлечений
        for s in student_data.split(';'): # разделяем строку на студентов
            part = s.split(':')
            students.append(Student(part[0], part[1])) # добавляем студентов и увлечения в список
        result = ""
        nameAdded = False
        for stu in students: # перебираем студентов
            nameAdded = False
            for book, theme in self.books.items(): # перебираем книги
                for subj in stu.interests: # перебираем интересы            
                    if subj == theme:
                        if nameAdded == False:
                            result = result.rstrip(' ,')
                            result += f";{stu.name}:"
                        nameAdded = True
                        result += f"{book}," # нужно перенести дальше, и добавлять только если есть книги
        return result.strip(';,')

def CreateBookLists(data:str)->str:
    students = [] # список студентов и увлечений
    for s in data.split('\n')[0].split(';'): # разделяем строку на студентов
        part = s.split(':')
        students.append(Student(part[0], part[1])) # добавляем студентов и увлечения в список    
    books = dict() # словарь книг и их разделов
    for o in data.split('\n')[1].split(';'): # делим список на отдельные книги
        book = o.split(':')
        books[book[0]] = book[1] # добавляем книгу в словарь
    result = ""
    nameAdded = False
    for stu in students: # перебираем студентов
        nameAdded = False
        for book, theme in books.items(): # перебираем книги
            for subj in stu.interests: # перебираем интересы            
                if subj == theme:
                    if nameAdded == False:
                        result = result.rstrip(' ,')
                        result += f";{stu.name}:"
                    nameAdded = True
                    result += f"{book}," # нужно перенести дальше, и добавлять только если есть книги
    return result.strip(';,') # не используется. Добавил весь функционал в класс Library

student_data = input()
# book_data = input()
student_data = "Анна:Научная фантастика,Математика;Иван:История,Документальная литература"
book_data = "Преступление и наказание:Художественная литература;Задача трёх тел:Научная фантастика;История государства российского:История"
school_library = Library(book_data) # исправлена строчная буква
# result = CreateBookLists(student_data)
# print(result)
print(school_library.compile_list(student_data))