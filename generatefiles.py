with open ("animals-list.txt", "a+") as animalsfile:
    animals=animalsfile.readlines()
animalsfile.close()

processedLetters = []
lettersToArray = {}

for animal in animals:
    animal = animal.replace('\n','').replace('\r','')
    print animal
    firstLetter = animal[0].upper()
    if firstLetter not in processedLetters:
        lettersToArray[firstLetter] = []
        processedLetters.append(firstLetter)
    lettersToArray[firstLetter].append(animal)

for letter in lettersToArray:

    animalfile = open('animals-by-letter/' + letter, "w+")
    animalfile.write("\t".join(lettersToArray[letter]))
    animalfile.close()
