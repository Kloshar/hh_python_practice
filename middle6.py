# coding=windows-1251 
# ����� �������� �������
import re
class TextProcessor:
    def __init__(self, text):
        self.text = text

    def extract_emails(self):        
        pattern1 = re.compile(r'[a-z1-9_\.-]+@[a-z1-9_\.-]+\.(?:ru|com|org|net)', flags=re.IGNORECASE)
        result = re.findall(pattern1, self.text)

        if len(result) > 0:
            for adress in result:
                print(adress)
        else:
            print("�� �������")

#input_text = input()
input_text = "��� ����� � email user123@example.com � user456@mail.ru, �� �� example.com"
input_text = "��� ������ ������ � ����������� ��������: userQ, Qdomain.com"
input_text = "��� ����� � email 123@example.com � ���������� ������� �������."
input_text = "����� ��� email-�������"

processor = TextProcessor(input_text)
processor.extract_emails()