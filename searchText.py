import re

# dict
counter = {}

# re
def getWordsByRe(words):
    return [w for w in re.compile("(?x) ( [\w-]+  | [\x80-\xff]{3} )").split(words) if w]

# load data from file
def loadDataFromFile(num):
    with open("alice_chapter"+num+".txt", "r") as f:
        global counter
        for line in f:
            for word in getWordsByRe(line):
                if word in counter: counter[word] += 1
                else:counter[word] = 1

# search words from dict
def searchByWords(words):
    resultCounter = {}
    global counter
    for word in getWordsByRe(words):
        resultCounter[word] = counter[word]

    return resultCounter


if __name__ == '__main__':
    # input file name
    for i in range(1,13):
        loadDataFromFile(str(i))


    # sort result dict
    wordsCounter = sorted([(counter,word) for word,counter in counter.items()],reverse=True)
    print(wordsCounter)

    # find words from data
    resultCounter = searchByWords("Who is alice")
    print(resultCounter)
