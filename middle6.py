# coding=windows-1251 
# ����� �������� �������
import re
class TextProcessor:
    def __init__(self, text):
        self.text = text

    def extract_emails(self):
        
        pattern1 = re.compile(r'[a-z]+', flags=re.IGNORECASE)

        result = re.findall(pattern1, self.text)

        print(result)

        #print("�� �������")

#input_text = input()

input_text = "��� ����� � email user123@example.com � user456@mail.ru, �� �� example.com"
# input_textxt = "��� ������ ������ � ����������� ��������: userQ, Qdomain.com"
# input_textxt = "��� ����� � email 123@example.com � ���������� ������� �������."
# input_textxt = "����� ��� email-�������"

processor = TextProcessor(input_text)
processor.extract_emails()