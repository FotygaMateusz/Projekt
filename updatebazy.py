import string
import MySQLdb
import pandas as pd
import csv

def update(db_connection, cur):

    df = pd.read_csv('results.csv', delimiter=',')

    types = df['tournament'].unique()

    cur.execute('DELETE FROM CITY')
    cur.execute('DELETE FROM TYPE_OF_GAME')
    cur.execute('DELETE FROM COUNTRY')
    cur.execute('DELETE FROM NAME_TEAM')
    cur.execute('SET FOREIGN_KEY_CHECKS = 0;')
    cur.execute('TRUNCATE TABLE CITY')
    cur.execute('TRUNCATE TABLE COUNTRY')
    cur.execute('TRUNCATE TABLE NAME_TEAM')
    cur.execute('TRUNCATE TABLE TYPE_OF_GAME')
    cur.execute('SET FOREIGN_KEY_CHECKS = 1;')


    for val in types:
        cur.execute('INSERT INTO TYPE_OF_GAME(TYPE_NAME) VALUES("%s");' % val)
    db_connection.commit()

    cities = df['city'].unique()

    for val in cities:
        newstrg = ""
        acc = """ '",{}[].`;:  """
        for x in val:
            if x in string.ascii_letters or x in string.digits or x in acc:
                newstrg += x
        cur.execute('INSERT INTO CITY(CITY_TYPE) VALUES("%s");' % (newstrg))
    db_connection.commit()

    country = df['country'].unique()


    for val in country:
        cur.execute('INSERT INTO COUNTRY(COUNTRY_TYPE) VALUES("%s");' % val)
    db_connection.commit()




    team = pd.Series(list(df['home_team']) + list(df['away_team'])).unique()


    for val in team:
        newstrg = ""
        acc = """ '",{}[].`;:  """
        for x in val:
            if x in string.ascii_letters or x in string.digits or x in acc:
                newstrg += x
        cur.execute('INSERT INTO NAME_TEAM(NAME_TEAM) VALUES("%s");' % newstrg)
    db_connection.commit()