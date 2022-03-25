import pytest 
from transactions import Transaction, to_transaction_dict

@pytest.fixture
def dbfile(tmpdir):
    ''' create a database file in a temporary file system '''
    return tmpdir.join('test_tracker.db')

@pytest.fixture
def empty_db(dbfile):
    ''' create an empty database '''
    db = Transaction(dbfile)
    yield db

@pytest.fixture
def small_db(empty_db):
    ''' create a small database, and tear it down later'''
    trans1 = {'amount': '25', 'category':'food', 'date': '20170120',  'description':'groceries and takeout'}
    trans2 = {'amount': '63', 'category':'car', 'date': '20170125',  'description':'wash and new tire'}
    trans3 = {'amount': '47', 'category':'fun', 'date': '20170130',  'description':'movies and dining out'}
    id1=empty_db.add(trans1)
    id2=empty_db.add(trans2)
    id3=empty_db.add(trans3)
    yield empty_db
    empty_db.delete(id3)
    empty_db.delete(id2)
    empty_db.delete(id1)

@pytest.fixture
def med_db(small_db):
    ''' create a database with 10 more elements than small_db'''
    rowids=[]
    # add 10 transactions
    for i in range(10):
        s = str(i)
        trans ={'amount': 'amount'+s, 'category':'category'+s, 'date': 'date'+s,  'description':'description'+s
                }
        rowid = small_db.add(trans)
        rowids.append(rowid)

    yield small_db

    # remove those 10 transegories
    for j in range(10):
        small_db.delete(rowids[j])



@pytest.mark.simple
def test_to_trans_dict():
    ''' teting the to_trans_dict function '''
    a = to_transaction_dict((7,'testamount','testcat','testdate','testdescription'))
    assert a['rowid']==7
    assert a['amount']=='testamount'
    assert a['category']=='testcat'
    assert a['date'] == 'testdate'
    assert a['description']== 'testdescription'
    assert len(a.keys())==5


@pytest.mark.add
def test_add(med_db):
    ''' add a transaction to db, then select it, then delete it'''

    trans0 = {'amount': '25', 'category':'test_add', 
              'date': '20170120',  'description':'please work'
            }
    transactions0 = med_db.select_all()
    rowid = med_db.add(trans0)
    transactions1 = med_db.select_all()
    assert len(transactions1) == len(transactions0) + 1
    trans1 = med_db.select_one(rowid)
    assert trans1['amount']==trans0['amount']
    assert trans1['category']==trans0['category']
    assert trans1['date']==trans0['date']
    assert trans1['description']==trans0['date']

@pytest.mark.delete
def test_delete(med_db):
    ''' add a transaction to db, delete it, and see that the size changes'''
    # first we get the initial table
    transactions0 = med_db.select_all()

    # then we add this transaction to the table and get the new list of rows
    trans0 = {'amount': '25', 'category':'testing_delete', 
              'date': '20170120',  'description':'groceries and takeout'
            }
    rowid = med_db.add(trans0)
    transactions1 = med_db.select_all()

    # now we delete the transaction and again get the new list of rows
    med_db.delete(rowid)
    transactions2 = med_db.select_all()

    assert len(transactions0)==len(transactions2)
    assert len(transactions2) == len(transactions1)-1

# @pytest.mark.update
# def test_summarize_by_date(med_db):

