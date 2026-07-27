#imports python package
import re
from pathlib import Path

folder_path = input("Provide path to folder with article .txt files: ")
directory = Path(folder_path)

#creates a list of the paths to all the txt files
texts = []
for i in range(30):
    texts.append(directory / f"Paper{i+1}.txt")

#creates a dictionary to houes the counts for each article/txt file
all = {}
articles = []

#adds each numbered article/txt file to the list of articles
for i in range(30):
    articles.append("article" + str(i+1))

#list of keywords to search per market driven and tenure conversion mechanisms
key_market = ["rent gap", "rent-gap", "private renovation", "upgrad", "mortgage lend", "rent", "tourism", "airbnb", "luxury", "real estate", "speculat", "land value", "flip", "landlord", "private capital", "private equity", "venture capital", "return on investment", "market rate", "migra", "disinvest", "reinvest"]
key_tenure = ["state led", "state-led", "city led", "public housing", "demoli", "relocat", "dispossess", "commodif", "regenerat", "slum clearance", "tenure reform", "renew", "expropriat", "resettle", "municipal", "decant", "permanent hous", "temporary hous", "state polic"]

key_all = key_market + key_tenure 

#initializes the counts of all the words for each article/txt file to 0
for article in articles:
    all[article] = dict([(x, 0) for x in key_all])

#loops through all the articles/txt files
for i in range(len(texts)):
    text = texts[i]
    temparticle = "article" + str(i+1)

    #reads each article/txt file to add a count for every word from the content list it finds
    with open(text) as f:
        content = " ".join(f.read().lower().split())

    for key_phrase in all[temparticle]:
        all[temparticle][key_phrase] = content.count(key_phrase) 

    #counts up the number of keywords that appear more than twice
    num_market = sum(1 for key_phrase in key_market if all[temparticle].get(key_phrase) > 2)
    num_tenure = sum(1 for key_phrase in key_tenure if all[temparticle].get(key_phrase) > 2)

    #prints yes or no based off if the num meets the threshold of consideration for market driven vs tenure conversion vs tourist driven mechanisms
    if (num_market/len(key_market)) > 3/22 :
        yn_market = "yes"
    else:
        yn_market = "no"

    if (num_tenure/len(key_tenure)) > 2/19 :
        yn_tenure = "yes"
    else:
        yn_tenure = "no"

    #prints the article and each of its nums              
    print(
    f"{temparticle}: \n"
    f"Market driven: {num_market}/{len(key_market)}, {yn_market} \n"
    f"Tenure conversion: {num_tenure}/{len(key_tenure)}, {yn_tenure} \n \n"
    )
