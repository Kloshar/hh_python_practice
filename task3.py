# coding=windows-1251
def check_password(password)->bool:
    spec_symbols = "!@#$%^&*(),.?\":{}|<>"

    cond = [False, False, False, False]

    if(len(password) > 7): cond[0] = True

    for ch in password:
        if(ch.isupper()): cond[1] = True

    for ch in password:
        if(ch.isdigit()): cond[2] = True
      
    for ch in password:
        for sy in spec_symbols:
            if(ch == sy): cond[3] = True

    if all(map(bool, cond)): return "Подходит"
    else: return "Не подходит"

#password = input()
password = "Password123!"
result = check_password(password)
print(result)