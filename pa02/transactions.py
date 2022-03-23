import sqlite3

def to_cat_dict(transaction_tuple):
    ''' cat is a category tuple (rowid, name, desc)'''
    transaction = {'item #':transaction_tuple[0], 'amount':transaction_tuple[1], 'category':transaction_tuple[2], 'date':transaction_tuple[3], 'description': transaction_tuple[4]}
    return cat

def to_cat_dict_list(cat_tuples):
    ''' convert a list of category tuples into a list of dictionaries'''
    return [to_cat_dict(cat) for cat in cat_tuples]

class Transaction:

    def __init__(self, dbfile):
        con= sqlite3.connect(dbfile)
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS categories
                    (name text, desc text)''')
        con.commit()
        con.close()
        self.dbfile = dbfile

    def select_all(self):
        ''' return all of the transactions as a list of dicts.'''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT rowid,* from ")
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_cat_dict_list(tuples)
        