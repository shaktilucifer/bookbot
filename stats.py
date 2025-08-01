def get_words(filePath):
    words = []
    with open(filePath, 'r') as file:
        words = file.read().split()
    return words

def get_char_map(words):
    myDict = {}
    count = 0
    for word in words:
        # print(word)
        for ch in word.lower():
            if ch in myDict:
                myDict[ch] += 1
            else:
                myDict[ch] = 1
    # print(myDict)
    return myDict


                
def printReport(wordCount, dict, bookPath):
    print("============ BOOKBOT ============")
    print("Analyzing book found at {bookPath}...".format(bookPath = bookPath))
    print("----------- Word Count ----------")
    print("Found {wordCount} total words".format(wordCount= wordCount))
    print("--------- Character Count -------")
    
    
    for key in sorted(dict, key=dict.get, reverse=True):
        print("{key}: {value}".format(key=key, value = dict[key]))
    print("============= END ===============")
