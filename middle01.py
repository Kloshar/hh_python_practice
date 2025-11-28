# coding=windows-1251 
# Работа с матрицами
def format_matrix (matrix_string: str)->str:
    lst = matrix_string.split(',')
    rows = int(lst[0])
    cols = int(lst[1])
    _str = ""

    for r in range(0,rows):
        for c in range(0, cols):
            #print(round(float(lst[2 + r*cols + c]),3))
            _str += str(round(float(lst[2 + r*cols + c]),3))
            _str += " "
        _str += "\n"
    return _str

#matrix_string = input()
matrix_string = "3,4,1.1349,2.6879,3.99999,4.5678,5.8712,6.00001,7.19231,8.123012,5.8712,6.00001,7.19231,1.66666"
formatted_matrix = format_matrix(matrix_string)
print(formatted_matrix)