import collections

# первый способ
phrase = "Python is the best language ever"
abv = ""
for i in phrase:
    if i not in abv:
        print(f"{i}: {phrase.count(i)}")
        abv += i

# 2 самые встречающиеся буквы через "import collections"

results = collections.Counter(phrase).most_common(2) 
print(results)
