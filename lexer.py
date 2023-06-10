tokenList = {
    "int": int,
    "str": str,
    '"': "sep",
    "'": 'sep',
    'printf': 'keyword',
    'var': 'keyword',
    '(': 'sep',
    ')': 'sep',
}


def createCharList(line):
    charList = []
    for word in line:
        for char in word:
            charList.append(char)
    return charList


def findValInQuote(line):
    charList = createCharList(line)
    inQuotes = False
    quoteCounter = 0
    tempStr = ''
    for charIndex, char in enumerate(charList):
        if char == '(' or char == ')':
            inQuotes = True
            quoteCounter += 1
            if quoteCounter % 2 == 0:
                inQuotes = False
        if inQuotes:
            tempStr += char
    return tempStr


def lexer(line):
    tokens = {}
    wordList = line.split(' ')
    for wordIndex, word in enumerate(wordList):
        if '(' in word or ')' in word:
            tokens['str'] = findValInQuote(line)
        if word == "printf":
            tokens['keyword'] = 'printf'
            tokens['val'] = wordList[wordIndex + 1]
        elif word == 'var':
            tokens['keyword'] = 'var'
            tokens['id'] = wordList[wordIndex + 1]
        elif word == '=':
            tokens['op'] = '='
            tokens['val'] = wordList[wordIndex + 1]
    return tokens