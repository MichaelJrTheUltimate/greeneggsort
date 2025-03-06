# def greenEggs():
#     infile = open("greeneggs.txt", "r")
#     wordList =[]

#     for line in infile: 
#         line = line.strip()

#         print(line)
#         words = line.split(" ")
#         wordList = wordList + words
#     infile. close()

#     UniqueWords = set(wordList)
#     print(UniqueWords)
#     print(len(UniqueWords))
#     print("The number of unique words in the file is", len(UniqueWords))
#     print("The number of words in the file is", len(wordList))
# greenEggs()
# co pilot told me of the "set" function to remove duplicates
#I decided to remake the code without the set function to try it myself
def greenEggs():
    infile = open("greeneggs.txt", "r")
    wordList = []

    for line in infile: 
        line = line.strip()
        print(line)
        line = line.replace("-", " ")  # Replace "-" with space
        words = line.split(" ")
        words = [word.strip(",.!?'") for word in words]
        words = [word.lower() for word in words]
        wordList = wordList + words
    infile.close()

    uniqueWordList = []
    for word in wordList:
        if word not in uniqueWordList:
            uniqueWordList.append(word)

    print(uniqueWordList)
    print(len(uniqueWordList))
    print("The number of unique words in the file is", len(uniqueWordList)-1)
    print("The number of words in the file is", len(wordList)-1)

greenEggs()