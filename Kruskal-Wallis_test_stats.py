#import python packages
import scipy.stats as stats
import numpy as np
from scipy.stats import chi2

#outputs the H-value for the data set of the differences in population
def population():
    #data sets
    new_pop = np.array([3.02, 11.32, 7.17])
    sing_pop = np.array([20.8, 28.4, 36.48])

    new_pop_ranks = np.array([1, 2, 3])
    sing_pop_ranks = np.array([4, 5, 6])

    #calculates the sum of the data sets
    new_pop_sum = np.sum(new_pop_ranks)
    sing_pop_sum = np.sum(sing_pop_ranks)

    #calculates the H-value using the Kruskal-Wallis statistical test
    sum = (new_pop_sum**2)/3 + (sing_pop_sum**2)/3
    h_value_pop = ((12/(6*(6+1)))*sum)-3*(6+1)

    print("H-value of population: " + str(h_value_pop))

    p_value = chi2.sf(h_value_pop, 1)

    print("P-value: " + str(p_value))

#outputs the H-value for the data set of the differences in income
def income():
    #data sets
    new_income = np.array([24.54, 48.06, 26.97])
    sing_income = np.array([40.96, 43.05, 39.11])

    new_income_ranks = np.array([1, 6, 2])
    sing_income_ranks = np.array([4, 5, 3])

    #calculates the sum of the data sets
    new_income_sum = np.sum(new_income_ranks)
    sing_income_sum = np.sum(sing_income_ranks)
    
    #calculates the H-value using the Kruskal-Wallis statistical test
    sum = (new_income_sum**2)/3 + (sing_income_sum**2)/3
    h_value_income = ((12/(6*(6+1)))*sum)-3*(6+1)

    #print H-values
    print("H-value of income:" + str(h_value_income))

    p_value = chi2.sf(h_value_income, 1)

    print("P-value: " + str(p_value))

population()
income()

