import sqlite3


def connect():
    conn=sqlite3.connect("songs.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (song_id INTEGER PRIMARY KEY, song_name TEXT NOT NULL, track_len INTEGER NOT NULL, artist TEXT NOT NULL, album TEXT NOT NULL)")
    conn.commit()
    conn.close()

def insert(name,track_len,artist,album):
    conn=sqlite3.connect("songs.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book (song_name, track_len, artist, album) VALUES (?,?,?,?)", (name,track_len,artist,album))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("songs.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book ")
    rows=cur.fetchall()
    conn.close()
    return rows

connect()
insert('Bombtrack', 340, 'RATM', 'RATM')
print(view())
