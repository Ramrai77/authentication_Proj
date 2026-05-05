from db import mysql

def create_user(name, email, password):
    cur = mysql.connection.cursor()
    cur.execute(
        "INSERT INTO users(name, email, password) VALUES(%s, %s, %s)",
        (name, email, password)
    )
    mysql.connection.commit()
    cur.close()

def get_user_by_email(email):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE email=%s", (email,))
    user = cur.fetchone()
    cur.close()
    return user