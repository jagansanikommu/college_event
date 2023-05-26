import sqlite3 as sql
from os import path
from datetime import datetime


ROOT = path.dirname(path.relpath((__file__)))

def create_post(mail,query):
    con=sql.connect(path.join(ROOT,'database.db'))
    cun = con.cursor()
    cun.execute('insert into querries(mail, query) values(?, ?)', (mail, query))
    con.commit()
    con.close()
    
def get_posts():
    con=sql.connect(path.join(ROOT,'database.db'))
    cun = con.cursor()
    cun.execute('select * from querries')
    posts = cun.fetchall()
    return posts
