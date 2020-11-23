#from sentiment_analysis5 import compute_tweets

#keywords = input("enter a keyword file: ")
#tweets = input("enter a tweet file: ")
keywords = 'data/keywords.txt'
tweets = 'data/tweets.txt'
emptyList = []
try:
        keyContents = open(keywords,"r",encoding="utf-8")
        #sorting keywords into the dictionary
        for line in keyContents:
            for line in keyContents:
                parts = line.lower()
                parts = parts.split(",")
                keyword = parts[0]
                value = int(parts[1])
            keyContents[keyword] = value
        keyContents.close()

except IOError:
    print("Error: the file", keywords, "does not exist.")

print(keywords)
