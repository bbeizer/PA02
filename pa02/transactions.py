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
        ''' return all of the categories as a list of dicts.'''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT rowid,* from categories")
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_cat_dict_list(tuples)
        