# coding=windows-1251
# Учебник по геометрии
def is_right_triangle(side_string: str)->bool:
    sides = list(map(int, side_string.split()))
    c = max(sides)
    sides.pop(sides.index(c))
    a = sides[0]
    b = sides[1]
    if(a**2+b**2==c**2): return True
    else: return False
side_string = input().strip()
if(is_right_triangle(side_string)): print('Да')
else: print('Нет')