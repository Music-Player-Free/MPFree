import sqlite3
from abc import ABC, abstractmethod
# from dataclasses import dataclass

from constants import DB_PATH

'''
TODO:
test that all implementations work as needed (scared about tags)
'''

class Database:
    # Init class variable path to database file
    # if not present SQLite3 will create file with this name.
    
    def __init__(self):
        self.table = ""
        self.columns = ""

        # Init connection to database (con)
        # Init cursor to database
        self.con = sqlite3.connect(DB_PATH)

        # Create tables if not already existing (error checking using sqlite convention 'IF NOT EXISTS')
        self.create_tables()


    def create_tables(self):
        '''
        Create tables for database file. \n
        Please note that the formatting is single-line to avoid redundant whitespacing.
        To see the properly formatted schemas (tables) please go to "/src/schema.txt."
        '''
        cur = self.con.cursor()
        cur.execute('''
                        CREATE TABLE IF NOT EXISTS songs (id INTEGER PRIMARY KEY, path_to_file TEXT NOT NULL, song_name TEXT NOT NULL,track_len INTEGER NOT NULL, artist TEXT NOT NULL,album TEXT NOT NULL)
                        ''')

        cur.execute('''
                        CREATE TABLE IF NOT EXISTS tags (id INTEGER PRIMARY_KEY NOT NULL, name TEXT NOT NULL,colour TEXT NOT NULL)
                        ''')

        cur.execute('''
                        CREATE TABLE IF NOT EXISTS collections  (id INTEGER PRIMARY KEY NOT NULL,name TEXT NOT NULL,description TEXT NOT NULL, author TEXT NOT NULL)
                        ''')

        cur.execute('''
                        CREATE TABLE IF NOT EXISTS songs_tags (idx INTEGER PRIMARY KEY NOT NULL, songs_id INT NOT NULL, tags_id INT NOT NULL, FOREIGN KEY(songs_id) REFERENCES songs(id), FOREIGN KEY(tags_id) REFERENCES tags(id))
                        ''')

        cur.execute('''
                        CREATE TABLE IF NOT EXISTS songs_collections (idx INTEGER PRIMARY KEY NOT NULL, songs_id INT NOT NULL, collections_id INT NOT NULL, FOREIGN KEY(songs_id) REFERENCES songs(id), FOREIGN KEY(collections_id) REFERENCES songs(id))
                        ''')

        cur.execute('''
                        CREATE TABLE IF NOT EXISTS collections_tags(idx INTEGER PRIMARY KEY NOT NULL, collections_id INT NOT NULL, tags_id INT NOT NULL, FOREIGN KEY(collections_id) REFERENCES collections(id), FOREIGN KEY(tags_id) REFERENCES tags(id))
                        ''')
        cur.close()
        self.con.commit()


    # Context manager stuff
    def __enter__(self):
        # "With" keyword call, when we "enter" an indentation space, we will return the instantiated (we know it
        # is an instance as we are using the convention "self", not "cls").
        return self

    # Context manager cont.j
    # Maybe use ext_type & traceback
    def __exit__(self, ext_type, exc_value, traceback):
        # If we pass in an exception, use the isinstance built-in function to decide if we revert any changes
        # (changes are .execute() statements) or if we commit them to the database (write them to memory).
        if isinstance(exc_value, Exception):
            self.con.rollback()
            exit(ext_type, traceback)
        else:
            self.con.commit()

        # Free connection regardless of if we had an error.
        self.con.close()

    def __repr__(self):
        return "Connected to {}".format(DB_PATH)


class DBInter(ABC):
    @abstractmethod
    def create(cls: 'Database', data: list) -> None:
        '''
        Insert data (list of values to pass in i.e. ["path", "darude sandstorm"...]) into table.
        '''
        cur = cls.con.cursor()
        sql = "INSERT INTO {} ({}) VALUES ({})".format(cls.table,
                                                       ", ".join(cls.columns[1:]), 
                                                       ', '.join(['?']*len(cls.columns[1:]))
                                                       )
        
        cur.execute(sql, data)
        cur.close()
        cls.con.commit()

    @abstractmethod
    def delete(cls: 'Database', id: int) -> None:
        '''
        Delete from databse using id value as int.
        '''
        cur = cls.con.cursor()
        sql = "DELETE FROM {} WHERE id in ?".format(cls.table)
        cur.execute(sql, (str(id),))
        cur.close()
        cls.con.commit()

    @abstractmethod
    def read(cls: 'Database', id: list[int]) -> sqlite3.Cursor:
        cur = cls.con.cursor()
        sql = "SELECT {} FROM {} WHERE id IN ({})".format(", ".join(cls.columns),
                                                    cls.table,
                                                    ", ".join("?" for _ in range(len(id))))
        return cur.execute(sql, id)

    @abstractmethod
    def read_all(cls: 'Database') -> sqlite3.Cursor:
        cur = cls.con.cursor()
        sql = "SELECT {} FROM {}".format(", ".join(cls.columns), 
                                        cls.table)
        return cur.execute(sql)
    


# Songs implementation of database connection
class SongDB(Database, DBInter):
    '''
    Database object for songs table.
    '''
    def __init__(self):
        super().__init__()
        self.table = "songs"
        self.columns = ["id", "path_to_file", "song_name", "track_len", "artist"]

    def create(self, data: list):
        return super().create(data)
    
    def delete(self, id: list[int]):
        return super().delete(id)
    
    def read(self, id: list[int]):
        return super().read(id)
    
    def read_all(self):
        return super().read_all()
    

    def __repr__(self):
        return "{} table ".format(self.table) + super().__repr__()



class TagDB(Database, DBInter):
    '''
    Database object for songs table.
    '''
    def __init__(self):
        # init database object (create tables, establish connection and cursor)
        super().__init__()

        # Create instance variable for table name and columns
        self.table = "tags"
        self.columns = ["id", "name", "colour"]

    def create(self, data):
        return super().create(data)
    
    def delete(self, id):
        return super().delete(id)
    
    def read(self, id):
        return super().read(id)
    
    def read_all(self):
        return super().read_all()
    

    def __repr__(self):
        return "{} table ".format(self.table) + super().__repr__()



class CollectionDB(Database, DBInter):
    '''
    Database object for songs table.
    '''
    def __init__(self):
        super().__init__()

        # Create instance variable for table name and columns
        self.table = "collections"
        self.columns = ["id", "name", "description", "author"]

    def create(self, data):
        return super().create(data)
    
    def delete(self, id):
        return super().delete(id)
    
    def read(self, id):
        return super().read(id)
    
    def read_all(self):
        return super().read_all()

    def __repr__(self):
        return "{} table ".format(self.table) + super().__repr__()

# ------------------------------------------------------- #

class RelationInter(ABC):
    @abstractmethod
    def read(self: 'Database', index: int, id: list[int]):
        '''
        Read from relation table. Index is strictly either 0 or 1. \n
        0/1 maps to the words in table name, <br>
        songs_collections maps 0 to songs and 1 maps to collections.
        '''
        cur = self.con.cursor()

        # Create args 
        assert 0 <= index <= 1
        assert isinstance(id, list)

        args = [self.columns[1 + ((index + i) % 2)] for i in range(2)] # either [1,2] or [2,1]
        args.insert(1, self.table)

        sql = "select {} from {} where {} = ?".format(*args)
        
        ans = cur.execute(sql, id)
        return ans


class Songs_Tags(Database, RelationInter): 
    def __init__(self):
        super().__init__()

        self.table = "songs_tags"
        self.columns = ["idx", "songs_id", "tags_id"]

    def __repr__(self):
        return "{} table ".format(self.table) + super().__repr__()
    


class Songs_Collections(Database, RelationInter):
    def __init__(self):
        super().__init__()

        self.table = "songs_collections"
        self.columns = ["idx", "songs_id", "collections_id"]

    def read(self, index, id):
        return super().read(index, id)
        
    def __repr__(self):
        return "{} table ".format(self.table) + super().__repr__()
    


class Collections_Tags(Database, DBInter):
    def __init__(self):
        super().__init__()

        self.table = "collections_tags"
        self.columns = ["idx", "collections_id", "tags_id"]

        
    def __repr__(self):
        return "{} table ".format(self.table) + super().__repr__()
