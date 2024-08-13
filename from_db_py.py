import sqlite3 as sql

con= sql.connect('from_db.db')
cur= con.cursor()
cur.execute('Drop table if exists test')

sql = '''create table "users"(
    "id" integer primary key autoincrement,
    "nome" text,
    "genero" text,
    "ano" text,
    "Plataforma" text)'''
cur.execute(sql)
con.commit()
con.close()