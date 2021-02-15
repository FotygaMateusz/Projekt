import string
import MySQLdb
import pandas as pd
import csv

def gam(db_connection, cur):
    df = pd.read_csv('results.csv', delimiter=',')
    cur.execute('DELETE FROM GAME')
    cur.execute('TRUNCATE TABLE GAME')


    cur.execute('SELECT * FROM CITY;')
    db_city = cur.fetchall()
    cur.execute('SELECT * FROM COUNTRY;')
    db_country = cur.fetchall()
    cur.execute('SELECT * FROM NAME_TEAM;')
    db_name = cur.fetchall()
    cur.execute('SELECT * FROM TYPE_OF_GAME;')
    db_type = cur.fetchall()

    game_date = df['date']
    # print(game_date)
    # print(db_city)
    # print(df['home_team'][0])
    counter = 0;

    for index,val in enumerate(game_date):
        for name in db_name:
            if df['home_team'][index] == name[1]:
                tmp_name_home = name[0]
            if df['away_team'][index] == name[1]:
                tmp_name_away = name[0]
        for type in db_type:
            if df['tournament'][index] == type[1]:
                tmp_type = type[0]
        for city in db_city:
            if df['city'][index] == city[1]:
                tmp_city = city[0]
        for country in db_country:
            if df['country'][index] == country[1]:
                tmp_country = country[0]
        cur.execute('INSERT INTO `game`(`GAME_DATE`, `HOME_TEAM_NAME_ID`, `AWAY_TEAM_NAME_ID`, `HOME_SCORE`, `AWAY_SCORE`, `TYPE_OF_GAME_ID`, `CITY_ID`, `COUNTRY_ID`, `NEUTRAL`) VALUES ("%s",%s,%s,%s,%s,%s,%s,%s,%s);' % (val,tmp_name_home,tmp_name_away,df['home_score'][index],df['away_score'][index],tmp_type,tmp_city,tmp_country,df['neutral'][index]))
        db_connection.commit()
        counter = counter +1
        if counter >10000:
            break









