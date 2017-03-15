with open ("animals-list.txt", "a+") as animalsfile:
    animals=animalsfile.read().split('\n')
animalsfile.close()

processedLetters = []

for animal in animals:
    print animal
    firstLetter = animal[0].upper()
    if firstLetter not in processedLetters:
        animalfile = open('animals-by-letter/' + firstLetter, "w+")
        animalfile.write('')
        animalfile.close()
        processedLetters.append(firstLetter)
    animalfile = open('animals-by-letter/' + firstLetter, "a+")
    animalfile.write(animal + "\n")
    animalfile.close()
