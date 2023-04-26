import pandas as pd
import numpy as np


chat_id = 752592494 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    from scipy.stats import t

    alpha = 0.02
    mu = 500
    n = len(x)
    x_bar = np.mean(x)
    s = np.std(x, ddof=1)

    t_stat = (x_bar - mu) / (s / np.sqrt(n))
    p_val = 1 - t.cdf(t_stat, n-1)

    if p_val < alpha:
        return True
    else:
        return False

    #another solution:
    #одновыборочный критерий z-тест
    
    def solution(x):
    res = ztest(x1=x, value=500, alternative='larger')
    return res[1] < 0.02
