import sqlite3


def init_database():
    # Warning: This file is created in the current directory
    con = sqlite3.connect('db/sessions.db')
    con.execute("CREATE TABLE session (id INTEGER PRIMARY KEY, name char(100) NOT NULL, url char(1024) NOT NULL, content char(1024), status bool NOT NULL)")
    con.commit()
