# coding=windows-1251 
# Поиск почтовых адресов
import re
class TextProcessor:
    def __init__(self, text):
        self.text = text

    def extract_emails(self):
        
        pattern1 = re.compile(r'\w')



        print("Не найдено")

#input_text = input()

input_text = "Это текст с email user123@example.com и user456@mail.ru, но не example.com"
# input_textxt = "Это пример текста с невалидными адресами: userQ, Qdomain.com"
# input_textxt = "Это текст с email 123@example.com и некоторыми другими данными."
# input_textxt = "Текст без email-адресов"

processor = TextProcessor(input_text)
processor.extract_emails()