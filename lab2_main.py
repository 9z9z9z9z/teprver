import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.stats.weightstats as w

if __name__ == '__main__':
    ws = pd.read_excel("lab2_excel.xlsx")
    df = pd.DataFrame(ws)
    df = df.astype(float)
    arr = df.to_numpy()
    arr = np.concatenate(arr, axis=0)
    Sorted = np.sort(arr)

    mean = np.mean(Sorted)
    var = np.var(Sorted, ddof=1)
    print('Выборочное среднее: ', mean)
    print('Выборочная дисперсия: ', np.var(Sorted, ddof=0))
    print('Исправленная выборочная дисперсия: ', var)


    print("\nНегруппированная выборка:")

    alpha = 0.05
    print('Доверительный интервал для мат ожидания')
    print(w.zconfint(Sorted, alpha=0.05, alternative="two-sided"))


    chi_l, chi_r = stats.chi2.ppf([1-alpha/2, alpha/2], df=49)
    left = 49 * var / chi_l
    right = 49 * var / chi_r
    print('Доверительный интервал для дисперсии')
    print("( ", left, right, " )")

    print("\nГруппированная выборка:")
    t1 = 2.0096
    x = 6.1
    S = 69.4286
    leftgr = x - t1 * S**(1/2) / (50)**(1/2)
    rightgr = x + t1 * S**(1/2) / (50)**(1/2)
    print('Доверительный интервал для мат ожидания')
    print("( ", leftgr, rightgr, " )")
    left = 49 * S / chi_l
    right = 49 * S / chi_r
    print('Доверительный интервал для дисперсии')
    print("( ", left, right, " )")
    print(var**0.5)
    print(mean+0.5*var**0.5)
