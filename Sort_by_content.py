import re

texts = []
for i in range(2):
    texts.append("/home/kay/Paper" + str(i) + ".txt")

all = {}
articles = []

for i in range(2):
    articles.append("article" + str(i))

content = ["gentrification", "was"]

for article in articles:
    all[article] = dict([(x, 0) for x in content])

for i in range(2):
    text = texts[i]
    temparticle = "article" + str(i)
    
    with open(text) as f:
        for line in f:
            for word in re.findall("\w+", line.lower()):
                if word in all[temparticle]:
                   all[temparticle][word] += 1
                   
    print(f"{temparticle}: {all[temparticle]}")

    
    if ((all[temparticle]["gentrification"]) > 1) :
        print("Mechanism of gentrification: Market-driven")

