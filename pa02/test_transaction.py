'''
test_transegories runs unit and integration tests on the transegory module
'''

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
    trans1 = {'amount': '25', 'category':'food', 'date': '20170120',  'desc':'groceries and takeout'}
    trans2 = {'amount': '63', 'category':'car', 'date': '20170125',  'desc':'wash and new tire'}
    trans3 = {'amount': '47', 'category':'fun', 'date': '20170130',  'desc':'movies and dining out'}
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
        trans ={'name':'name'+s,
               'desc':'description '+s,
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
    a = to_transaction_dict((7,'testtrans','testdesc'))
    assert a['rowid']==7
    assert a['name']=='testtrans'
    assert a['desc']=='testdesc'
    assert len(a.keys())==3


@pytest.mark.add
def test_add(med_db):
    ''' add a transegory to db, the select it, then delete it'''

    trans0 = {'name':'testing_add',
            'desc':'see if it works',
            }
    transs0 = med_db.select_all()
    rowid = med_db.add(trans0)
    transs1 = med_db.select_all()
    assert len(transs1) == len(transs0) + 1
    trans1 = med_db.select_one(rowid)
    assert trans1['name']==trans0['name']
    assert trans1['desc']==trans0['desc']


@pytest.mark.delete
def test_delete(med_db):
    ''' add a transegory to db, delete it, and see that the size changes'''
    # first we get the initial table
    transs0 = med_db.select_all()

    # then we add this transegory to the table and get the new list of rows
    trans0 = {'name':'testing_add',
            'desc':'see if it works',
            }
    rowid = med_db.add(trans0)
    transs1 = med_db.select_all()

    # now we delete the transegory and again get the new list of rows
    med_db.delete(rowid)
    transs2 = med_db.select_all()

    assert len(transs0)==len(transs2)
    assert len(transs2) == len(transs1)-1

@pytest.mark.update
def test_update(med_db):
    ''' add a transegory to db, updates it, and see that it changes'''

    # then we add this transegory to the table and get the new list of rows
    trans0 = {'name':'testing_add',
            'desc':'see if it works',
            }
    rowid = med_db.add(trans0)

    # now we upate the transegory
    trans1 = {'name':'new trans','desc':'new desc'}
    med_db.update(rowid,trans1)

    # now we retrieve the transegory and check that it has changed
    trans2 = med_db.select_one(rowid)
    assert trans2['name']==trans1['name']
    assert trans2['desc']==trans1['desc']
