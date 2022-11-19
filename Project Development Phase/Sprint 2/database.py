import sqlite3 

class Database:
    def __init__(self):
        self.con = sqlite3.connect('static/database/storage.db')
        self.cur = self.con.cursor()
        self.cur.execute("create table if not exists users(name varchar, email varchar, password varchar)")
        self.con.commit()
    
    def creeateUser(self, name, email, password):
        self.cur.execute("insert into users values('" + name + "', '" + email + "', '" + password + "')")
        self.con.commit()

    def loginUser(self, email):
        self.cur.execute("select password from users where email = '" + email + "'")
        userData = self.cur.fetchone()
        return userData


db = Database()