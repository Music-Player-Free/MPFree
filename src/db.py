import sqlite3


class Database:
    # TODO: 
    # File organisation, path might change.
    DB_PATH = "mpfree.db"
    def __init__(self, user_filename):
        # set up connection
        self.con = sqlite3.connect(self.DB_PATH)
        self.cur = self.con.cursor()

        self.user_filename = user_filename

    def create(self):
        self.cur.execute('''
                        CREATE TABLE IF NOT EXISTS songs (id INTEGER PRIMARY KEY, song_name TEXT NOT NULL,track_len INTEGER NOT NULL, artist TEXT NOT NULL,album TEXT NOT NULL);
                        ''')
        
        self.cur.execute('''
                        CREATE TABLE IF NOT EXISTS tags (id INT PRIMARY_KEY NOT NULL, name TEXT NOT NULL,colour TEXT NOT NULL);
                        ''')
        
        self.cur.execute('''
                        CREATE TABLE IF NOT EXISTS collections  (id INT PRIMARY KEY NOT NULL,name TEXT NOT NULL,description TEXT NOT NULL,author);
                        ''')

        self.cur.execute('''
                        CREATE TABLE IF NOT EXISTS songs_tags (idx INT PRIMARY KEY NOT NULL, songs_id INT NOT NULL, tags_id INT NOT NULL, FOREIGN KEY(songs_id) REFERENCES songs(id), FOREIGN KEY(tags_id) REFERENCES tags(id),);
                        ''')
        
        self.cur.execute('''
                        CREATE TABLE IF NOT EXISTS songs_collections (idx INT PRIMARY KEY NOT NULL, songs_id INT NOT NULL, collections_id INT NOT NULL, FOREIGN KEY(songs_id) REFERENCES songs(id), FOREIGN KEY(collections_id) REFERENCES songs(id));
                        ''')
        
        self.cur.execute('''
                        CREATE TABLE IF NOT EXISTS collections_tags(idx INT PRIMARY KEY NOT NULL, collections_id INT NOT NULL, tags_id INT NOT NULL, FOREIGN KEY(collections_id) REFERENCES collections(id), FOREIGN KEY(tags_id) REFERENCES tags(id));
                        ''')

    def insert(self, data):
        pass


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

with Database() as db:
    db.create()
