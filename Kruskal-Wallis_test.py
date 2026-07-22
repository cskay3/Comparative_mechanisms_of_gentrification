import scipy.stats as stats
import numpy as np

def population():
    new_pop = np.array([3.02, 11.32, 7.17])
    sing_pop = np.array([20.8, 28.4, 36.48])

    new_pop_sum = np.sum(new_pop)
    sing_pop_sum = np.sum(sing_pop)
    sum = (new_pop_sum**2)/3 + (sing_pop_sum**2)/3
    value_pop = ((12/(6*(6+1)))*sum)-3*(6+1)

    print("H-value of population:" + str(value_pop))

def income():
    new_income = np.array([24.54, 48.06, 26.97])
    sing_income = np.array([40.96, 43.05, 39.11])

    new_income_sum = np.sum(new_income)
    sing_income_sum = np.sum(sing_income)
    sum = (new_income_sum**2)/3 + (sing_income_sum**2)/3
    value_income = ((12/(6*(6+1)))*sum)-3*(6+1)

    print("H-value of income:" + str(value_income))

population()
income()

