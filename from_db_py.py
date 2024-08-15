import sqlite3 as sql

con = sql.connect('from_db.db')
cur = con.cursor()

cur.execute('''drop table if exists users''')

sql = '''create table "users"(
    "id" integer primary key autoincrement,
    "nome" text,
    "genero" text,
    "ano" text,
    "Plataforma" text)'''
cur.execute(sql)

sql = '''insert into users(nome, genero, ano, plataforma) values
    ('The Last of Us', 'Ação', '2013', 'PS4'),
    ('The Legend of Zelda', 'Adventure', '1986', 'NES'),
    ('Super Mario Bros.', 'Platformer', '1985', 'NES'),
    ('Minecraft', 'Sandbox', '2011', 'PC'),
    ('Final Fantasy VII', 'RPG', '1997', 'PlayStation'),
    ('The Witcher 3: Wild Hunt', 'RPG', '2015', 'PC'),
    ('Halo: Combat Evolved', 'FPS', '2001', 'Xbox'),
    ('God of War', 'Action', '2018', 'PlayStation 4'),
    ('Red Dead Redemption 2', 'Action-Adventure', '2018', 'PlayStation 4'),
    ('Cyberpunk 2077', 'RPG', '2020', 'PC'),
    ('Among Us', 'Party', '2018', 'PC'),
    ('Fortnite', 'Battle Royale', '2017', 'PC'),
    ('Overwatch', 'FPS', '2016', 'PC'),
    ('Genshin Impact', 'RPG', '2020', 'PC'),
    ('Apex Legends', 'Battle Royale', '2019', 'PC')'''
cur.execute(sql)

con.commit()
con.close()
