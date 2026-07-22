#imports python package
import re

#creates a list of the paths to all the txt files
texts = []
for i in range(2):
    texts.append("/home/kay/Paper" + str(i) + ".txt")

#creates a dictionary to houes the counts for each article/txt file
all = {}
articles = []

#adds each numbered article/txt file to the list of articles
for i in range(2):
    articles.append("article" + str(i))

#list of keywords to search
content = ["gentrification", "was"]

#initializes the counts of all the words for each article/txt file to 0
for article in articles:
    all[article] = dict([(x, 0) for x in content])

#loops through all the articles/txt files
for i in range(2):
    text = texts[i]
    temparticle = "article" + str(i)

    #reads each article/txt file to add a count for every word from the content list it finds
    with open(text) as f:
        for line in f:
            for word in re.findall("\w+", line.lower()):
                if word in all[temparticle]:
                   all[temparticle][word] += 1
                   
    #prints the article and its count for each word               
    print(f"{temparticle}: {all[temparticle]}")

    #Characterizs clusters and quantities of specific words from the content list as a category of mechanism of gentrification
    if ((all[temparticle]["gentrification"]) > 1) :
        print("Mechanism of gentrification: Market-driven")

