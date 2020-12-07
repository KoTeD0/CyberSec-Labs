import sqlite3

def login(login, password, signal):
    con = sqlite3.connect('db/users')
    cur = con.cursor()

    #проверяем есть ли такой пользователь
    cur.execute(f'SELECT * FROM users WHERE login="{login}";')
    value = cur.fetchall()

    if value != [] and value[0][2] == password:
        signal.emit('Успешная авторизация!')
    else:
        signal.emit('Проверьте правильность ввода данных!')

    cur.close()
    con.close()