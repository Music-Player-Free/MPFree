import sqlite3


class Database:
    # TODO:
    # File organisation, path might change.
    DB_PATH = "src/mpfree.db"
    def __init__(self):
        # set up connection
        self.con = sqlite3.connect(self.DB_PATH)
        self.cur = self.con.cursor()
        self.create_tables()


    def create_tables(self):
        self.cur.execute('''
                        CREATE TABLE IF NOT EXISTS songs (id INTEGER PRIMARY KEY, path_to_file TEXT NOT NULL, song_name TEXT NOT NULL,track_len INTEGER NOT NULL, artist TEXT NOT NULL,album TEXT NOT NULL)
                        ''')

        self.cur.execute('''
                        CREATE TABLE IF NOT EXISTS tags (id INT PRIMARY_KEY NOT NULL, name TEXT NOT NULL,colour TEXT NOT NULL)
                        ''')

        self.cur.execute('''
                        CREATE TABLE IF NOT EXISTS collections  (id INT PRIMARY KEY NOT NULL,name TEXT NOT NULL,description TEXT NOT NULL,author)
                        ''')
        
        self.cur.execute('''
                        CREATE TABLE IF NOT EXISTS songs_tags (idx INT PRIMARY KEY NOT NULL, songs_id INT NOT NULL, tags_id INT NOT NULL, FOREIGN KEY(songs_id) REFERENCES songs(id), FOREIGN KEY(tags_id) REFERENCES tags(id))
                        ''')

        self.cur.execute('''
                        CREATE TABLE IF NOT EXISTS songs_collections (idx INT PRIMARY KEY NOT NULL, songs_id INT NOT NULL, collections_id INT NOT NULL, FOREIGN KEY(songs_id) REFERENCES songs(id), FOREIGN KEY(collections_id) REFERENCES songs(id))
                        ''')

        self.cur.execute('''
                        CREATE TABLE IF NOT EXISTS collections_tags(idx INT PRIMARY KEY NOT NULL, collections_id INT NOT NULL, tags_id INT NOT NULL, FOREIGN KEY(collections_id) REFERENCES collections(id), FOREIGN KEY(tags_id) REFERENCES tags(id))
                        ''')
        self.con.commit()


    # Context manager stuff
    def __enter__(self):
        return self

    # Context manager cont.
    # Maybe use ext_type & traceback
    def __exit__(self, ext_type, exc_value, traceback):
        self.cur.close()
        if isinstance(exc_value, Exception):
            self.con.rollback()
        else:
            self.con.commit()
        self.con.close()
        

# Songs implementation of database connection
class SongDB(Database):
    def __init__(self):
        super().__init__()
        self.table = "songs"
        self.columns = ["path_to_file", "song_name", "track_len", "artist", "album"]

    def create(self, data: list) -> None:
        sql = "INSERT INTO {} ({}) VALUES ({})".format(self.table, ", ".join(self.columns), ', '.join(['?']*len(self.columns)))
        self.cur.execute(sql, data)
        self.con.commit()

    def delete(self, id: int) -> None:
        # try:
        #     str(id)
        #     pass
        # except ValueError:
        #     pass

        sql = "DELETE FROM {} WHERE id = ?".format(self.table)
        self.cur.execute(sql, (str(id),))
        self.con.commit()

    def read(self, id: int) -> list:
        # for safe keeping:
        # ', '.join(self.columns)
        sql = "SELECT * FROM songs WHERE id = ?".format(self.table)
        res = self.cur.execute(sql, (str(id),))
        return res.fetchall()


from Songs import Song
path = "path-to-file"
song_name = "title"
track_len = 302
artist = "artist"
album = "album"
s = None
with SongDB() as db:
    db.create_tables()
    db.create([path, song_name, track_len, artist, album])
    db.create([path, song_name, track_len, artist, album])


    '''
    TODO
    Some work to be done here lads. Thinking of sending through **kwargs into songs
    objects so that we can just straight up tuple(res) this shit.
    '''
    # res = db.read(db.cur.lastrowid)
    # s = Song(*tuple(res))



# x = Song("")

