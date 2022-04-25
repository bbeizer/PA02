import sqlite3

def to_transaction_dict(transaction_tuple):
    ''' transaction is a transaction tuple (item_id, amount, category, date, description) '''
    transaction = {'rowid':transaction_tuple[0], 'amount':transaction_tuple[1], 'category':transaction_tuple[2], 'date':transaction_tuple[3], 'desc': transaction_tuple[4]}
    return transaction

def to_transaction_dict_list(transaction_tuples):
    ''' convert a list of transaction tuples into a list of dictionaries'''
    return [to_transaction_dict(transaction) for transaction in transaction_tuples]

class Transaction:

    def __init__(self, dbfile):
        con= sqlite3.connect(dbfile)
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS transactions
                    (amount text, category text, date text, desc text)''')
        con.commit()
        con.close()
        self.dbfile = dbfile

    def select_all(self):
        ''' return all of the transactions as a list of dicts.'''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT rowid,* from transactions")
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_transaction_dict_list(tuples)

    def delete(self,rowid):
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''DELETE FROM transactions
                       WHERE rowid=(?);
        ''',(rowid,))
        con.commit()
        con.close()

    def add(self,item):
        ''' add a transaction to the transactions table.
            this returns the rowid of the inserted element
        '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("INSERT INTO transactions VALUES(?,?,?,?)",(item['amount'], item['category'], item['date'], item['desc']))
        con.commit()
        cur.execute("SELECT last_insert_rowid()")
        last_rowid = cur.fetchone()
        con.commit()
        con.close()
        return last_rowid[0]
    
    def summarize_by_date(self):
        ''' summarizes transactions by date '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''SELECT date, SUM(amount) FROM transactions GROUP BY date''')
        tuples = cur.fetchall()
        con.commit()
        con.close()
        result = {'date': tuples[0], 'total_transaction': tuples[1]}
        return [result for tup in tuples]
    
    def summarize_by_month(self):
        ''' summarize transactions by month'''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''SELECT SUBSTRING(date, 5,2), SUM(amount) from transactions GROUPBY SUBSTRING(date, 5,2)''')
        tuples = cur.fetchall()
        con.commit()
        con.close()
        result = {'date': tuples[0], 'total_transaction': tuples[1]}
        return [result for tup in tuples]

    def summarize_by_year(self):
        '''summarizes transactions by year'''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''SELECT SUBSTRING(date, 1,4), SUM(amount) from transactions GROUPBY SUBSTRING(date, 1,4)''')
        tuples = cur.fetchall()
        con.commit()
        con.close()
        result = {'date': tuples[0], 'total_transaction': tuples[1]}
        return [result for tup in tuples]

    def summarize_by_cat(self):
        '''summarizes by category'''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''SELECT category, SUM(amount) FROM transactions GROUP BY category''')
        tuples = cur.fetchall()
        con.commit()
        con.close()
        result = {'category': tuples[0], 'total_transaction': tuples[1]}
        return [result for tup in tuples]

