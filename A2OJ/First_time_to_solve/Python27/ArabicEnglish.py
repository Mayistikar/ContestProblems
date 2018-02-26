from sys import stdin, stdout


def isEnglishWord(listWords):
    for word in listWords:
        if word.count('#') == 0:
            return listWords.index(word)
    return 200


def printSentence(listWords, indexWord, endWord):
    if endWord:
        firstWord = listWords[indexWord]
        secondWord = ' '.join(listWords[0:indexWord])
        return firstWord+" "+secondWord
    firstWord = ' '.join(listWords[indexWord+1:len(listWords)])
    secondWord = listWords[indexWord]
    thirdWord = ' '.join(listWords[0:indexWord])
    return firstWord+" "+secondWord+" "+thirdWord


def main():

    test_cases = int(stdin.readline())

    for test_case in range(test_cases):

        line = stdin.readline()
        words = stdin.readline()
        listWords = words.split()
        indexEnglishWord = isEnglishWord(listWords)

        if indexEnglishWord == 200:
            stdout.write(words)
        elif indexEnglishWord == len(listWords)-1:
            stdout.write(printSentence(listWords, indexEnglishWord, True)+"\n")
        else:
            stdout.write(printSentence(listWords, indexEnglishWord, False)+"\n")


main()
