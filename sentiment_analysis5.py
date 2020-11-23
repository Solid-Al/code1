
f = open('Data/keywords.txt')
keyContents = f.read()
keyContents = keyContents.split(',')

f.close()
#print(keyContents)

p = open('Data/tweets.txt')
tweetContents = p.read()
#tweetContents = tweetContents.split('\n')
p.close()

#for line in keyContents:
#      divide the line into word and value
#      assign the values to variables
#      dictionary[word] = value

keyContents = {}
for line in keyContents:
    parts = line.lower()
    parts = parts.split(",")
    keyword = parts[0]
    value = int(parts[1])
    keyContents[keyword] = value
    print(keyContents)

for line in tweetContents:
    partsOne = line.split(" ",5)
    #latitude = (float(partsOne[0].lstrip("[").rstrip(",")))
    #tweet = partsOne[5].lower().strip()
    print(partsOne[0].lstrip("[").rstrip(","))
#print(tweetContents)
