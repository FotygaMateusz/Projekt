import stat
import pandas as pd
import numpy as np
import scipy.stats as scs
import statistics as st
import matplotlib.pyplot as plt
from scipy.stats import normaltest
from scipy import stats
from math import log


def stat(db_connection, cur):
    df = pd.read_csv('results.csv', delimiter=',')


    cur.execute('SELECT * FROM GAME;')
    db_game = cur.fetchall()
    listt = []
    for ea in db_game:
        listt.append(ea[4])
        listt.append(ea[5])
    # print('min = ',np.min(listt))
    # print('maximum of goals = ',np.max(listt))
    # print('std = ',np.std(listt))
    # print('mean = ',np.mean(listt))
    cur.execute('SELECT HOME_SCORE,AWAY_SCORE FROM GAME;')
    db_goals = cur.fetchall()
    print('----------------------Statystyka--------------------------------')
    print('sum of goals = ',np.sum(db_goals))
    print('min = ',np.min(db_goals))
    print('max = ',np.max(db_goals))
    print('std = ',np.std(db_goals))
    print('mean = ',np.mean(db_goals))
    # cur.execute('SELECT * from GAME where `HOME_SCORE` = %s OR `AWAY_SCORE` = %s;' %(np.max(db_goals),np.max(db_goals)))
    # print(cur.fetchall())


    # stat, p = normaltest(db_goals)
    # print("Normal test: p= ",  p)

    # Test t-studenta dla dwóch prób niezależnych:
    test_1 = stats.ttest_ind(db_goals[0], db_goals[1])
    print("niezaleznych = ", test_1[1])
    # Test t-studenta dla dwóch prób zależnych:
    test_2 = stats.ttest_rel(db_goals[0], db_goals[1])
    print("zaleznych = ", test_2[1])
    print('----------------------7--------------------------------')
    cur.callproc('groupp')
    a = pd.DataFrame(cur.fetchall())

    p1 = plt.bar(a[0], a[1])
    p2 = plt.bar(a[0], a[2])
    plt.ylabel('Goals')
    plt.title('Goals in years scored by Home/Away teams')
    plt.legend((p1[0], p2[0]), ('Home', 'Away'))
    plt.show()

