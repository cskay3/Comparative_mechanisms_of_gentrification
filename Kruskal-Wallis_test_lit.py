#import python packages
import scipy.stats as stats

#outputs the H-value for the values of market-driven mechanism
def market():
    #data sets
    north = [17.5, 24, 24, 12.5, 24, 17.5, 12.5, 6.5, 24, 24]
    south = [17.5, 12.5, 17.5, 6.5, 12.5, 24, 24, 29.5, 6.5, 17.5]
    east = [6.5, 1.5, 1.5, 28, 6.5, 6.5, 6.5, 29.5, 17.5, 6.5]

    #kruskal-wallis function
    statistic, pvalue = stats.kruskal(north, south, east)

    print("H-value of market-driven: " + str(statistic))
    print("P-value: " + str(pvalue))

#outputs the H-value for the values of tenure-conversion mechanism
def tenure():
    #data sets
    north = [2.5, 16, 23.5, 16, 8, 8, 8, 8, 16, 28.5]
    south = [28.5, 16, 2.5, 16, 8, 23.5, 16, 27, 8, 16]
    east = [23.5, 16, 16, 8, 2.5, 30, 23.5, 23.5, 2.5, 23.5]

    #kruskal-wallis function
    statistic, pvalue = stats.kruskal(north, south, east)

    print("H-value of tenure-conversion: " + str(statistic))
    print("P-value: " + str(pvalue))
    
market()
tenure()

