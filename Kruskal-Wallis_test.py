#import python packages
import scipy.stats as stats
import numpy as np

#outputs the H-value for the data set of the differences in population
def population():
    #data sets
    new_pop = np.array([3.02, 11.32, 7.17])
    sing_pop = np.array([20.8, 28.4, 36.48])

    #calculates the sum of the data sets
    new_pop_sum = np.sum(new_pop)
    sing_pop_sum = np.sum(sing_pop)

    #calculates the H-value using the Kruskal-Wallis statistical test
    sum = (new_pop_sum**2)/3 + (sing_pop_sum**2)/3
    value_pop = ((12/(6*(6+1)))*sum)-3*(6+1)

    print("H-value of population:" + str(value_pop))

#outputs the H-value for the data set of the differences in income
def income():
    #data sets
    new_income = np.array([24.54, 48.06, 26.97])
    sing_income = np.array([40.96, 43.05, 39.11])

    #calculates the sum of the data sets
    new_income_sum = np.sum(new_income)
    sing_income_sum = np.sum(sing_income)
    
    #calculates the H-value using the Kruskal-Wallis statistical test
    sum = (new_income_sum**2)/3 + (sing_income_sum**2)/3
    value_income = ((12/(6*(6+1)))*sum)-3*(6+1)

    #print H-values
    print("H-value of income:" + str(value_income))

population()
income()

