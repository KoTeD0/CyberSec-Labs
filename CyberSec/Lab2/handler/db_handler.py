import sqlite3


def logon(login, password, signal):
    con = sqlite3.connect('handler/users')
    cur = con.cursor()

    # Проверяем есть ли такой пользователь
    cur.execute(f'SELECT * FROM users WHERE login="{login}";')
    value = cur.fetchall()
    
    if value != [] and value[0][2] == int(password):
        signal.emit('Authorize Complete! ')
    else:
        signal.emit('Username or password wrong!')

    cur.close()
    con.close()


def register(login, password, name, last_name, born_date, born_place, phone, signal):
    con = sqlite3.connect('handler/users')
    cur = con.cursor()

    cur.execute(f'SELECT * FROM users WHERE login="{login}";')
    value = cur.fetchall()

    if value != []:
        signal.emit('That nick-name is already used!')

    elif value == []:
        cur.execute(f"INSERT INTO users (login, password, name, last_name, born_date, born_place, phone)"
                    f"VALUES ('{login}', '{password}','{name}','{last_name}','{born_date}','{born_place}','{phone}')")
        signal.emit('Registration successful!')
        con.commit()

    cur.close()
    con.close()

def change_pass(login, current_password, new_password, signal):
    con = sqlite3.connect('handler/users')
    cur = con.cursor()

    cur.execute(f'SELECT * FROM users WHERE login="{login}";')
    value = cur.fetchall()

    if value != [] and value[0][2] == int(current_password):
        cur.execute(f"UPDATE users SET password = '{int(new_password)+5}' Where login = '{login}'")
        con.commit()
        signal.emit('Values successfully changed')
    else:
        signal.emit('Passwords dont match!')

    cur.close()
    con.close()