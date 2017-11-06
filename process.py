megawordlist = []
wordcount = {}
boardlist = []

resultfile = open("test.txt", "r")
for line in resultfile:
    wordlist = line.rstrip().split(",")
    boardstring = wordlist.pop(0)
    print boardstring
    count = len(wordlist)
    points = 0
    for word in wordlist:
        if len(word) <= 4:
            points += 1
        elif len(word) == 5:
            points += 2
        elif len(word) == 6:
            points += 3
        elif len(word) == 7:
            points += 4
        elif len(word) >= 8:
            points += 11
        if word not in megawordlist:
            megawordlist.append(word)
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    boardlist.append([boardstring,count,points])

resultfile.close()
