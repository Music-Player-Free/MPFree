import sqlite3
from abc import ABC, abstractmethod
# from dataclasses import dataclass

'''
TODO:
implement relations tables as classes
add id's to songs (will know how we should do this when we get to using them...? (IDK!!!))

'''


class DBInter(ABC):
    @abstractmethod
    def generate_kwargs(self, data):
        d = {}
        for i, attr in enumerate(self.columns):
            d[str(attr)] = data[i]
        return d

class Database:
    # Init class variable path to database file
    # if not present SQLite3 will create file with this name.
    DB_PATH = "src/mpfree.db"
    def __init__(self):
        self.table = ""
        self.columns = ""

        # Init connection to database (con)
        # Init cursor to database
        self.con = sqlite3.connect(self.DB_PATH)

        # A cursor is SQLite's way of interacting with databases, using .execute() will act like a terminal window (in a sense).
        self.cur = self.con.cursor()

        # Create tables if not already existing (error checking using sqlite convention 'IF NOT EXISTS')
        self.create_tables()


    def create_tables(self):
        '''
        Create tables for database file. \n
        Please note that the formatting is single-line to avoid redundant whitespacing.
        To see the properly formatted schemas (tables) please go to "/src/schema.txt."
        '''
        self.cur.execute('''
                        CREATE TABLE IF NOT EXISTS songs (id INTEGER PRIMARY KEY, path_to_file TEXT NOT NULL, song_name TEXT NOT NULL,track_len INTEGER NOT NULL, artist TEXT NOT NULL,album TEXT NOT NULL)
                        ''')

        self.cur.execute('''
                        CREATE TABLE IF NOT EXISTS tags (id INTEGER PRIMARY_KEY NOT NULL, name TEXT NOT NULL,colour TEXT NOT NULL)
                        ''')

        self.cur.execute('''
                        CREATE TABLE IF NOT EXISTS collections  (id INTEGER PRIMARY KEY NOT NULL,name TEXT NOT NULL,description TEXT NOT NULL, author TEXT NOT NULL)
                        ''')

        self.cur.execute('''
                        CREATE TABLE IF NOT EXISTS songs_tags (idx INTEGER PRIMARY KEY NOT NULL, songs_id INT NOT NULL, tags_id INT NOT NULL, FOREIGN KEY(songs_id) REFERENCES songs(id), FOREIGN KEY(tags_id) REFERENCES tags(id))
                        ''')

        self.cur.execute('''
                        CREATE TABLE IF NOT EXISTS songs_collections (idx INTEGER PRIMARY KEY NOT NULL, songs_id INT NOT NULL, collections_id INT NOT NULL, FOREIGN KEY(songs_id) REFERENCES songs(id), FOREIGN KEY(collections_id) REFERENCES songs(id))
                        ''')

        self.cur.execute('''
                        CREATE TABLE IF NOT EXISTS collections_tags(idx INTEGER PRIMARY KEY NOT NULL, collections_id INT NOT NULL, tags_id INT NOT NULL, FOREIGN KEY(collections_id) REFERENCES collections(id), FOREIGN KEY(tags_id) REFERENCES tags(id))
                        ''')
        self.con.commit()


    # Context manager stuff
    def __enter__(self):

        # "With" keyword call, when we "enter" an indentation space, we will return the instantiated (we know it
        # is an instance as we are using the convention "self", not "cls").
        return self

    # Context manager cont.
    # Maybe use ext_type & traceback
    def __exit__(self, ext_type, exc_value, traceback):

        # Start by freeing the cursor (avoids mem leaks)
        self.cur.close()

        # If we pass in an exception, use the isinstance built-in function to decide if we revert any changes
        # (changes are .execute() statements) or if we commit them to the database (write them to memory).
        if isinstance(exc_value, Exception):
            self.con.rollback()
            exit(ext_type)
        else:
            self.con.commit()

        # Free connection regardless of if we had an error.
        self.con.close()

    def __repr__(self):
        return "Connected to {}".format(self.DB_PATH)


# Songs implementation of database connection
class SongDB(Database, DBInter):
    '''
    Database object for songs table.
    '''
    def __init__(self):
        # init database object (create tables, establish connection and cursor)
        super().__init__()

        # Create instance variable for table name and columns
        # This allows for quick modification and easier debugging.
        self.table = "songs"
        self.columns = ["path_to_file", "song_name", "track_len", "artist"]

    def create(self, data: list) -> None:
        '''
        Insert data (list of values to pass in i.e. ["path", "darude sandstorm"...] into table
        '''
        '''
        To insert into sql the syntax is:
        INSERT INTO _table_ (columns) VALUES (values);
        When using sqlite in python, we use the cursor.execute() method.
        This method takes two arguments:
            - a string representing the sql query to be executed,
            - and a list variable representing data to be passed into the sql query

        so we could do something like:
        sql_query_as_string = "INSERT INTO songs (path_to_file, album,...etc) VALUES (?, ?, ?, ?)"
        data = ["/workspace1/folder1/balls.mp3", "balls album", ...]

        cursor.execut(sql_query_as_string, data)

        the use of '?' in the sql string is a convention of Python sqlite3. The execute function will replace any '?'
        with the data you pass in.

        Since we might want to adjust the columns (or at least have the ability to do so, forward thinking and that)
        we take the length of columns variable and create a string of '?' characters separated by ", "
        this means if we change songs to have 12 columns, then we only have to update the columns and the (?, ?, ?, ?)
        will be generated dynamically.

        String method .join() works on the string literal ", " which is a comma and whitespace
        join takes a list as a parameter and will intersect the string between whatever is in the input list.
        Think of it as an opposite to split, "Here is sample".split(" ") returns ["Here", "is", "sample"]
        and ", ".join(["Here", "is", "sample"]) will return "Here, is, sample" (notice  how it doesn't add to the ends).
        '''

        sql = "INSERT INTO {} ({}) VALUES ({})".format(self.table, ", ".join(self.columns), ', '.join(['?']*len(self.columns)))
        self.cur.execute(sql, data)
        self.con.commit()

    def delete(self, id: int) -> None:
        '''
        Delete from databse using id value as int.
        '''


        # try:
        #     str(id)
        #     pass
        # except ValueError:
        #     pass

        # Will only ever have one '?' char as there is only one id.
        sql = "DELETE FROM {} WHERE id = ?".format(self.table)
        self.cur.execute(sql, (str(id),))
        self.con.commit()

    def read(self, id: int) -> list:
        # for safe keeping:
        # ', '.join(self.columns)
        sql = "SELECT * FROM {} WHERE id = ?".format(self.table)
        res = self.cur.execute(sql, (str(id),))
        return res.fetchall()

    #adding this because idk how to read iteratively in python without knowing the size of the table
    def read_all(self) -> list:
           # for safe keeping:
           # ', '.join(self.columns)
           sql = "SELECT * FROM {}".format(self.table)
           res = self.cur.execute(sql)
           return res.fetchall()

    def generate_kwargs(self, data):
        return super().generate_kwargs(data)

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
        self.columns = ["text", "colour"]

    def create(self, data: list) -> None:
        '''
        Insert data (list of values to pass in i.e. ["happy", "reddish brown"...] into table
        '''
        sql = "INSERT INTO {} ({}) VALUES ({})".format(self.table, ", ".join(self.columns), ', '.join(['?']*len(self.columns)))
        self.cur.execute(sql, data)
        self.con.commit()

    def delete(self, id: int) -> None:
        '''
        Delete from databse using id value as int.
        '''

        # Will only ever have one '?' char as there is only one id.
        sql = "DELETE FROM {} WHERE id = ?".format(self.table)

        self.cur.execute(sql, (str(id),))
        self.con.commit()

    def read(self, id: int) -> list:
        # for safe keeping:
        # ', '.join(self.columns)
        sql = "SELECT * FROM {} WHERE id = ?".format(self.table)

        res = self.cur.execute(sql, (str(id),))
        return res.fetchall()

    def generate_kwargs(self, data):
        return super().generate_kwargs(data)

    def __repr__(self):
        return "{} table ".format(self.table) + super().__repr__()


class CollectionDB(Database, DBInter):
    '''
    Database object for songs table.
    '''
    def __init__(self):
        # init database object (create tables, establish connection and cursor)
        super().__init__()

        # Create instance variable for table name and columns
        self.table = "collections"
        self.columns = ["name", "description", "author"]


    def create(self, data: list) -> None:
        '''
        Insert data (list of values to pass in i.e. ["collection2", "awesome playlist", "user2"] into table
        '''
        sql = "INSERT INTO {} ({}) VALUES ({})".format(self.table, ", ".join(self.columns), ', '.join(['?']*len(self.columns)))
        self.cur.execute(sql, data)
        self.con.commit()


    def delete(self, id: int) -> None:
        '''
        Delete from databse using id value as int.
        '''

        # Will only ever have one '?' char as there is only one id.
        sql = "DELETE FROM {} WHERE id = ?".format(self.table)
        self.cur.execute(sql, (str(id),))
        self.con.commit()

    def read(self, id: int) -> list:
        # for safe keeping:
        # ', '.join(self.columns)
        sql = "SELECT * FROM {} WHERE id = ?".format(self.table)
        res = self.cur.execute(sql, (str(id),))
        return res.fetchall()

    def generate_kwargs(self, data):
        return super().generate_kwargs(data)

    def __repr__(self):
        return "{} table ".format(self.table) + super().__repr__()





# Impromptu test code, import song to eventually read and construct song object from database.
# That has not been implemented yet.
#from Songs import Song
#path = "path-to-file"
#song_name = "title"
#track_len = 302
#artist = "artist"
#album = "album"
#s = None

# With __ as __ format is context manager. Anything within the indentation will
# begin the __enter__(), and anything outside, the interpreter will assume we are done (which we will be).
#with SongDB() as db:
#    db.create([path, song_name, track_len, artist, album])

    # generate kwargs?

#    res = db.read(db.cur.lastrowid)
#    attributes = db.generate_kwargs(res[0])
#    s = Song(**attributes)
#    print(s)


# x = Song("")

'''
Typically initialise this within the scope of a CRUD (Create, Read, Update, Delete) function.

However, at the bottom you will see two dunder ((D)ouble (UNDER)score) magic functions (https://www.geeksforgeeks.org/dunder-magic-methods-python/)
that are used for context managing (https://book.pythontips.com/en/latest/context_managers.html#context-managers).

This means that we can error handle by using the __exit__() function that checks whether we exited on purpose,
or if the program broke and threw an error.
'''
