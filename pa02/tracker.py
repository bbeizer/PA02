#! /opt/miniconda3/bin/python3
'''
tracker is an app that maintains a list of personal
financial transactions.

It uses Object Relational Mappings (ORM)
to abstract out the database operations from the
UI/UX code.

The ORM, Category, will map SQL rows with the schema
  (rowid, category, description)
to Python Dictionaries as follows:

(5,'rent','monthly rent payments') <-->

{rowid:5,
 category:'rent',
 description:'monthly rent payments'
 }

Likewise, the ORM, Transaction will mirror the database with
columns:
amount, category, date (yyyymmdd), description
In place of SQL queries, we will have method calls.
This app will store the data in a SQLite database ~/tracker.db
Note the actual implementation of the ORM is hidden and so it 
could be replaced with PostgreSQL or Pandas or straight python lists
'''

from transactions import Transaction
from category import Category

transactions = Transaction('tracker.db')
category = Category('tracker.db')


# here is the menu for the tracker app

MENU = '''
0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this menu
'''

def process_choice(choice):
    '''code for taking user input and allowing user to play around with category and transaction functions'''
    if choice=='0':
        return
    elif choice=='1':
        cats = category.select_all()
        print_categories(cats)
    elif choice=='2':
        print("add category")
        name = input("category name: ")
        desc = input("category description: ")
        cat = {'name':name, 'desc':desc}
        category.add(cat)
    elif choice=='3':
        print("modifying category")
        rowid = int(input("rowid: "))
        name = input("new category name: ")
        desc = input("new category description: ")
        cat = {'name':name, 'desc':desc}
        category.update(rowid,cat)
    elif choice=='4':
        print("show transactions")
        trans = transactions.select_all()
        print_transactions(trans)
    elif choice=='5':
        print("add transaction")
        amount = int(input("transaction amount: "))
        cat = input("transaction category: ")
        date = input("transaction date: ")
        desc = input("transaction description: ")
        transac = {'amount':amount, 'category':cat, 'date':date, 'desc': desc}
        transactions.add(transac)
    elif choice=='6':
        print("delete transaction")
        rowid = int(input("rowid to delete: "))
        transactions.delete(rowid)
    elif choice=='7':
        print("summarize transactions by date")
        date = input("enter date yyyymmdd: ")
        transac = transactions.summarize_by_date(date)
        print_summarize_by(transac, 'date', date)
    elif choice=='8':
        print("summarize transactions by month")
        month = input("enter month E.g 'mm': ")
        transac = transactions.summarize_by_month(month)
        print_summarize_by(transac, 'month', month)
    elif choice=='9':
        print("summarize transactions by year")
        year = input("enter year E.g 'yyyy': ")
        transac = transactions.summarize_by_year(year)
        print_summarize_by(transac, 'year', year)
    elif choice=='10':
        print("summarize transactions by category")
        cat = input("enter the category: ")
        transac = transactions.summarize_by_cat(cat)
        print_summarize_by(transac, 'category', cat)
    elif choice=='11':
        print("choices menu: ", MENU)
    else:
        print("choice",choice,"not yet implemented")
    choice = input("> ")
    return choice


def toplevel():
    ''' handle the user's choice '''

    print(MENU)
    choice = input("> ")
    while choice !='0' :
        choice = process_choice(choice)
    print('bye')

#
# here are some helper functions
#

def print_transactions(items):
    ''' print the transactions '''
    if len(items)==0:
        print('no items to print')
        return
    print('\n')
    print("%-10s %-10s %-10s %-10s %-30s"%(
        'item #','amount','category','date','description'))
    print('-'*40)
    for item in items:
        values = tuple(item.values()) 
        print("%-10s %-10s %-10s %-10s %-30s"%values)

def print_category(cat):
    '''prints a category'''
    print("%-3d %-10s %-30s"%(cat['rowid'],cat['name'],cat['desc']))

def print_categories(cats):
    '''Helper method to print categories'''
    print("%-3s %-10s %-30s"%("id","name","description"))
    print('-'*45)
    for cat in cats:
        print_category(cat)

def print_summarize_by(items, col, var):
    '''Prints summarize by methods'''
    print("%-10s %-10s" % (col, 'total transaction'))
    print('-' * 40)
    if col != 'category':
        for item in items:
            s1 ="amount: " + item[1] + "   "
            s2 ="category: " + item[2] + "   "
            s3 ="description: " + item[4] + "   "
            print("%-10s %-10s %-10s %-10s"% (var, s1,s2,s3))
    else:
        for item in items:
            s1 ="amount: " + item[1] + "   "
            s2 ="date: " + item[3] + "   "
            s3 ="description: " + item[4] + "   "
            print("%-10s %-10s %-10s %-10s"% (var, s1,s2,s3))






# here is the main call!
toplevel()

