import collections


phrase = "Python is the best language ever"
abv = ""
for i in phrase:
    if i not in abv:
        print(f"{i}: {phrase.count(i)}")
        abv += i

results = collections.Counter(phrase) # нашел через "import collections"
print(results)