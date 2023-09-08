import sqlite3

#builds a database with chosen name
def creat_database():
    name_database = input('Database Name- ')
    conn = sqlite3.connect(name_database+'.sqlite')
    cur = conn.cursor()

    cur.executescript('''
    DROP TABLE IF EXISTS Author;
    DROP TABLE IF EXISTS Title;
    DROP TABLE IF EXISTS Series;
    DROP TABLE IF EXISTS Genre;
    DROP TABLE IF EXISTS Publisher;

    CREATE TABLE Author (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
    );

    CREATE TABLE Title (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        Name TEXT UNIQUE,
        Author,
        Series,
        Sr_Num,
        Genre,
        Publisher,
        Num_Copys INTEGER
    );

    CREATE TABLE Series (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE,
        num_copys INTERGER
    );

    CREATE TABLE Genre (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
    );

    CREATE TABLE Publisher (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
    );

    ''')
    print('...Database Created...')
    conn.commit()
    conn.close()

#adds rows to the database
def Add_Book():
    name_database = input('Database Name You Want to Modify- ')
    conn = sqlite3.connect(name_database + '.sqlite')
    cur = conn.cursor()
    while True:
        add = input('Enter 1 to Continue or 2 to quite: ')
        add = int(add)
        if add == 2:
            break
        elif add >= 3:
            print('unknown command')
            continue
        elif add == 1:
            Author_Name = input('Add Author: ')
            cur.execute(''' 
            INSERT OR IGNORE INTO Author (name)
            VALUES (?) ''',
            (Author_Name, ) )
            conn.commit()

            Series_Name = input('Add Series: ')
            Book_Num = input('Add Series Num: ')
            cur.execute(''' 
            INSERT OR IGNORE INTO Series (name, num_copys)
            VALUES (?, ?) ''',
            (Series_Name, Book_Num, ))
            conn.commit()

            Genre_Name = input('Add Genre: ')
            cur.execute(''' 
            INSERT OR IGNORE INTO Genre (name)
            VALUES (?) ''',
            (Genre_Name, ))
            conn.commit()

            Publisher_Name = input('Add Publisher: ')
            cur.execute(''' 
            INSERT OR IGNORE INTO Publisher (name)
            VALUES (?) ''',
            (Publisher_Name, ))
            conn.commit()

            Title_Name = input('Add Title: ')
            Num_of = int(input('Number of copys: '))
            try:

                cur.execute(''' 
                INSERT INTO Title (Name, Author, Series, Sr_Num, Genre, Publisher, Num_Copys)
                VALUES (?, ?, ?, ?, ?, ?, ?) ''',
                (Title_Name, Author_Name, Series_Name, Book_Num, Genre_Name, Publisher_Name, Num_of, ) )
                conn.commit()
                print('Book Add..')
            except:
                print('Title already exist...')
            continue
        conn.commit()
        conn.close()
        print('...Library Updated...')

#prints out the whole database
def view():
    name_database = input('Database Name You Want to View- ')
    conn = sqlite3.connect(name_database + '.sqlite')
    cur = conn.cursor()

    cur.execute('SELECT * FROM Title')
    info = cur.fetchall()
    print('Total rows are: ', len(info))
    print('...Printing each row...')
    for row in info:
        print('Id: ', row[0])
        print('Name: ', row[1])
        print('Author: ', row[2])
        print('Series: ', row[3])
        print('Series Number: ', row[4])
        print('Genre: ', row[5])
        print('Publisher: ', row[6])
        print('Number of Copys: ', row[7])
        print('\n')
    
    conn.close()

#print out search results from database
def search():
    name_database = input('Database Name You Want to Search- ')
    conn = sqlite3.connect(name_database + '.sqlite')
    cur = conn.cursor()

    column = input('Choose column: Name, Author, Series, Genre, Publisher: ')
    search_word = input('Enter Search Term: ')
    cur.execute("SELECT * FROM Title WHERE " + column + " LIKE '%" + search_word + "%'")
    info = cur.fetchall()
    print('Total rows are: ', len(info))
    print('...Printing each row...')
    for row in info:
        print('Id: ', row[0])
        print('Name: ', row[1])
        print('Author: ', row[2])
        print('Series: ', row[3])
        print('Series Number: ', row[4])
        print('Genre: ', row[5])
        print('Publisher: ', row[6])
        print('Number of Copys: ', row[7])
        print('\n')

    conn.close()

#makes changes to colums in the database
def update():
     name_database = input('Database Name You Want to Update- ')
     conn = sqlite3.connect(name_database + '.sqlite')
     cur = conn.cursor()

     column = input('Choose column: Name, Author, Series,sr_num, Genre, Publisher, num_copys: ')
     value = input('New Value: ')
     id = input('Enter id of row: ')
     print(('UPDATED Title Column ' + column + 'New: ' + value + " WHERE id of Row = " + id))
     cur.execute('UPDATE Title SET ' + column + " =" + " '" + value + "' WHERE id = " + id + ';')
     conn.commit()
     conn.close()
     print('...Library Updated...')

#deletes whole rows in the database
def delete():
    name_database = input('Database Name You Want to Update- ')
    conn = sqlite3.connect(name_database + '.sqlite')
    cur = conn.cursor()

    id = input('Enter id of row you would like to delete or 0 to quite: ')
    id = int(id)
    if id >= 1:
        cur.execute('DELETE FROM Title WHERE id = ' + str(id) + ';')
        conn.commit()
        conn.close()
    elif id == 0:
        print('...Done...')
    else:
        print('Error: try again')

#main meanu for program
while True:
    start = input('1.Create Database-\n2.Add Book-\n3.View Database-\n4.Search Database-\n5.Update Datatbase-\n6.Delete Book-\n7.Quite-\nEnter: ')
    start = int(start)
    if start == 1:
        creat_database()
        continue
    elif start == 2:
        Add_Book()
        continue
    elif start == 3:
        view()
        continue
    elif start == 4:
        search()
        continue
    elif start == 5:
        update()
        continue
    elif start == 6:
        delete()
        continue
    elif start == 7:
        print('...Finished...')
        break
    else:
        print('Error: Not A Choice...')
        continue