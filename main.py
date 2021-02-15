import string
import MySQLdb
import pandas as pd
import csv
import scipy.stats as scs
import matplotlib.pyplot as plt
import updatebazy
import game
import statystyka

db_connection = MySQLdb.connect(host='localhost', user='root', passwd='', db='project')
cur = db_connection.cursor()


updatebazy.update(db_connection, cur)

game.gam(db_connection, cur)

statystyka.stat(db_connection, cur)

db_connection.close()
