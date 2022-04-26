# CS103a Spring 22

# PA02: tracker.py and the Transaction class

Our app maintains maintains a list of personal financial transactions. 
In tracker.py the User has the ability to add, delete, modify, and show all user categories and transactions in and SQLite database. 
In addition to this the user can search for transactions based on the date, month, and year the transaction was made. 
Our group mainly implemented the tracker.py and the transaction.py class

# A) Pylint

tracker.py:26:61: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:55:0: C0301: Line too long (109/100) (line-too-long)
tracker.py:141:37: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:178:0: C0304: Final newline missing (missing-final-newline)
tracker.py:56:4: R1705: Unnecessary "elif" after "return" (no-else-return)
tracker.py:54:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
tracker.py:54:0: R0912: Too many branches (13/12) (too-many-branches)
tracker.py:54:0: R0915: Too many statements (59/50) (too-many-statements)
tracker.py:161:12: C0103: Variable name "s1" doesn't conform to snake_case naming style (invalid-name)
tracker.py:162:12: C0103: Variable name "s2" doesn't conform to snake_case naming style (invalid-name)
tracker.py:163:12: C0103: Variable name "s3" doesn't conform to snake_case naming style (invalid-name)
tracker.py:167:12: C0103: Variable name "s1" doesn't conform to snake_case naming style (invalid-name)
tracker.py:168:12: C0103: Variable name "s2" doesn't conform to snake_case naming style (invalid-name)
tracker.py:169:12: C0103: Variable name "s3" doesn't conform to snake_case naming style (invalid-name)

------------------------------------------------------------------
Your code has been rated at 8.64/10 (previous run: 8/10, +.064)
(base) Ben@Benjamins-MacBook-Air pa02 % pylint tracker.py

************* Module tracker
tracker.py:26:61: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:55:0: C0301: Line too long (109/100) (line-too-long)
tracker.py:141:37: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:178:0: C0304: Final newline missing (missing-final-newline)
tracker.py:56:4: R1705: Unnecessary "elif" after "return" (no-else-return)
tracker.py:54:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
tracker.py:54:0: R0912: Too many branches (13/12) (too-many-branches)
tracker.py:54:0: R0915: Too many statements (59/50) (too-many-statements)

------------------------------------------------------------------
Your code has been rated at 9.22/10 (previous run: 8.93/10, +0.29)

# B) Pytest

(base) Ben@Benjamins-MacBook-Air pa02 % pytest -v
======================================================================= test session starts ========================================================================
platform darwin -- Python 3.8.8, pytest-6.2.3, py-1.10.0, pluggy-0.13.1 -- /Users/Ben/opt/anaconda3/bin/python
cachedir: .pytest_cache
rootdir: /Users/Ben/PA02/pa02, configfile: pytest.ini
plugins: anyio-2.2.0
collected 8 items                                                                                                                                                  

test_category.py::test_to_cat_dict PASSED                                                                                                                    [ 12%]
test_category.py::test_add PASSED                                                                                                                            [ 25%]
test_category.py::test_delete PASSED                                                                                                                         [ 37%]
test_category.py::test_update PASSED                                                                                                                         [ 50%]
test_transaction.py::test_to_trans_dict FAILED                                                                                                               [ 62%]
test_transaction.py::test_delete ERROR                                                                                                                       [ 75%]
test_transaction.py::test_summarize_by_date ERROR                                                                                                            [ 87%]
test_transaction.py::test_add ERROR                                                                                                                          [100%]

============================================================================== ERRORS ==============================================================================
__________________________________________________________________ ERROR at setup of test_delete ___________________________________________________________________

empty_db = <transactions.Transaction object at 0x7f8a687edac0>

    pytest.fixture
    def small_db(empty_db):
        ''' create a small database, and tear it down later'''
        trans1 = {'amount': '25', 'category':'food', 'date': '20170120',  'description':'groceries and takeout'}
        trans2 = {'amount': '63', 'category':'car', 'date': '20170125',  'description':'wash and new tire'}
        trans3 = {'amount': '47', 'category':'fun', 'date': '20170130',  'description':'movies and dining out'}
>       id1=empty_db.add(trans1)

test_transaction.py:21: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <transactions.Transaction object at 0x7f8a687edac0>, item = {'amount': '25', 'category': 'food', 'date': '20170120', 'description': 'groceries and takeout'}

    def add(self,item):
        ''' add a transaction to the transactions table.
            this returns the rowid of the inserted element
        '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
>       cur.execute("INSERT INTO transactions VALUES(?,?,?,?)",(item['amount'], item['category'], item['date'], item['desc']))
E       KeyError: 'desc'

transactions.py:48: KeyError
_____________________________________________________________ ERROR at setup of test_summarize_by_date _____________________________________________________________

empty_db = <transactions.Transaction object at 0x7f8a688604c0>

    @pytest.fixture
    def small_db(empty_db):
        ''' create a small database, and tear it down later'''
        trans1 = {'amount': '25', 'category':'food', 'date': '20170120',  'description':'groceries and takeout'}
        trans2 = {'amount': '63', 'category':'car', 'date': '20170125',  'description':'wash and new tire'}
        trans3 = {'amount': '47', 'category':'fun', 'date': '20170130',  'description':'movies and dining out'}
>       id1=empty_db.add(trans1)

test_transaction.py:21: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <transactions.Transaction object at 0x7f8a688604c0>, item = {'amount': '25', 'category': 'food', 'date': '20170120', 'description': 'groceries and takeout'}

    def add(self,item):
        ''' add a transaction to the transactions table.
            this returns the rowid of the inserted element
        '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
>       cur.execute("INSERT INTO transactions VALUES(?,?,?,?)",(item['amount'], item['category'], item['date'], item['desc']))
E       KeyError: 'desc'

transactions.py:48: KeyError
____________________________________________________________________ ERROR at setup of test_add ____________________________________________________________________

empty_db = <transactions.Transaction object at 0x7f8a6880cd30>

    @pytest.fixture
    def small_db(empty_db):
        ''' create a small database, and tear it down later'''
        trans1 = {'amount': '25', 'category':'food', 'date': '20170120',  'description':'groceries and takeout'}
        trans2 = {'amount': '63', 'category':'car', 'date': '20170125',  'description':'wash and new tire'}
        trans3 = {'amount': '47', 'category':'fun', 'date': '20170130',  'description':'movies and dining out'}
>       id1=empty_db.add(trans1)

test_transaction.py:21: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <transactions.Transaction object at 0x7f8a6880cd30>, item = {'amount': '25', 'category': 'food', 'date': '20170120', 'description': 'groceries and takeout'}

    def add(self,item):
        ''' add a transaction to the transactions table.
            this returns the rowid of the inserted element
        '''
        con= sqlite3.connect(self.dbfile)

(base) Ben@Benjamins-MacBook-Air pa02 % pytest -v
======================================================================= test session starts ========================================================================
platform darwin -- Python 3.8.8, pytest-6.2.3, py-1.10.0, pluggy-0.13.1 -- /Users/Ben/opt/anaconda3/bin/python
cachedir: .pytest_cache
rootdir: /Users/Ben/PA02/pa02, configfile: pytest.ini
plugins: anyio-2.2.0
collected 8 items                                                                                                                                                  

test_category.py::test_to_cat_dict PASSED                                                                                                                    [ 12%]
test_category.py::test_add PASSED                                                                                                                            [ 25%]
test_category.py::test_delete PASSED                                                                                                                         [ 37%]
test_category.py::test_update PASSED                                                                                                                         [ 50%]
test_transaction.py::test_to_trans_dict PASSED                                                                                                               [ 62%]
test_transaction.py::test_delete PASSED                                                                                                                      [ 75%]
test_transaction.py::test_summarize_by_date FAILED                                                                                                           [ 87%]
test_transaction.py::test_add FAILED                                                                                                                         [100%]

============================================================================= FAILURES =============================================================================
______________________________________________________________________ test_summarize_by_date ______________________________________________________________________

med_db = <transactions.Transaction object at 0x7fcf786dff40>

    @pytest.mark.update
    def test_summarize_by_date(med_db):
    
        # then we add this transegory to the table and get the new list of rows
        trans0 = {'amount':'testing_add',
                'category':'see if it works',
                'date':'19991203',
                'desc': 'this is a description'
                }
        rowid = med_db.add(trans0)
    
        # now we upate the transegory
        trans1 = {'amount':'testing_add','category':'see if it works','date':'19990421','desc':"this is a description"}
>       med_db.update(rowid,trans1)
E       AttributeError: 'Transaction' object has no attribute 'update'

test_transaction.py:116: AttributeError
_____________________________________________________________________________ test_add _____________________________________________________________________________

med_db = <transactions.Transaction object at 0x7fcf78752a00>

    def test_add(med_db):
        ''' add a transaction to db, then select it, then delete it'''
    
        trans0 = {'amount':'testing add',
                'category':'see if it works',
                'date':'19991203',
                'desc': 'this is a description'
                }
        trans0 = med_db.select_all()
>       rowid = med_db.add(trans0)

test_transaction.py:135: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <transactions.Transaction object at 0x7fcf78752a00>
item = [{'amount': '25', 'category': 'food', 'date': '20170120', 'desc': 'groceries and takeout', ...}, {'amount': '63', 'cat...': 'date1', 'desc': 'desc1', ...}, {'amount': 'amnt2', 'category': 'cat2', 'date': 'date2', 'desc': 'desc2', ...}, ...]

    def add(self,item):
        ''' add a transaction to the transactions table.
            this returns the rowid of the inserted element
        '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
>       cur.execute("INSERT INTO transactions VALUES(?,?,?,?)",(item['amount'], item['category'], item['date'], item['desc']))
E       TypeError: list indices must be integers or slices, not str

transactions.py:48: TypeError
===================================================================== short test summary info ======================================================================
FAILED test_transaction.py::test_summarize_by_date - AttributeError: 'Transaction' object has no attribute 'update'
FAILED test_transaction.py::test_add - TypeError: list indices must be integers or slices, not str
=================================================================== 2 failed, 6 passed in 0.39s ====================================================================
(base) Ben@Benjamins-MacBook-Air pa02 % pytest -v

# C) Tracker

> 5 
add transaction
transaction amount: 2000  
transaction category: cats
transaction date: 20040625
transaction description: I bought an OBSCENE amount of cats on this day
> 4
show transactions


item number     amount     category   date       description                   
----------------------------------------
1          5000       cats       19991203   I bought a ton of cats        
2          30         food       20000303   I bought an expensive meatball sub on this dates
3          20         clothes    19991203   bought a pair of shoes        
4          400        appliances 20051117   bought a new TV               
5          200        food       19991203   bought food for a superbowl party
6          2000       cats       20040625   I bought an OBSCENE amount of cats on this day
> 6
delete transaction
rowid to delete: 4
> 4
show transactions


item number     amount     category   date       description                   
----------------------------------------
1          5000       cats       19991203   I bought a ton of cats        
2          30         food       20000303   I bought an expensive meatball sub on this dates
3          20         clothes    19991203   bought a pair of shoes        
5          200        food       19991203   bought food for a superbowl party
6          2000       cats       20040625   I bought an OBSCENE amount of cats on this day
> 7
summarize transactions by date
enter date yyyymmdd: 19991203
date       total transaction
----------------------------------------
19991203   amount: 5000    category: cats    description: I bought a ton of cats   
19991203   amount: 20    category: clothes    description: bought a pair of shoes   
19991203   amount: 200    category: food    description: bought food for a superbowl party   
> 8
summarize transactions by month
enter month E.g 'mm': 11
month      total transaction
----------------------------------------
> 8
summarize transactions by month
enter month E.g 'mm': 03
month      total transaction
----------------------------------------
03         amount: 30    category: food    description: I bought an expensive meatball sub on this dates   
> 9
summarize transactions by year
enter year E.g 'yyyy': 1999
year       total transaction
----------------------------------------
1999       amount: 5000    category: cats    description: I bought a ton of cats   
1999       amount: 20    category: clothes    description: bought a pair of shoes   
1999       amount: 200    category: food    description: bought food for a superbowl party   
> 10
summarize transactions by category
enter the category: cats
category   total transaction
----------------------------------------
cats       amount: 5000    date: 19991203    description: I bought a ton of cats   
cats       amount: 2000    date: 20040625    description: I bought an OBSCENE amount of cats on this day  


