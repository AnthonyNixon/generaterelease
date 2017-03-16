def process(itemType):
    with open (itemType + "-list.txt", "a+") as listfile:
        items=listfile.readlines()
    listfile.close()

    processedLetters = []
    lettersToArray = {}

    for item in items:
        item = item.replace('\n','').replace('\r','')
        print item
        firstLetter = item[0].upper()
        if firstLetter not in processedLetters:
            lettersToArray[firstLetter] = []
            processedLetters.append(firstLetter)
        lettersToArray[firstLetter].append(item)

    for letter in lettersToArray:
        itemfile = open(itemType + '-by-letter/' + letter, "w+")
        itemfile.write("\t".join(lettersToArray[letter]))
        itemfile.close()

process('animals')
process('adjectives')
