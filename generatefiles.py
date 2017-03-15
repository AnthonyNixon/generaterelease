with open ("animals-list.txt", "a+") as animalsfile:
    animals=animalsfile.readlines()
animalsfile.close()

processedLetters = []

for animal in animals:
    animal = animal.replace('\n','').replace('\r','')
    print animal
    firstLetter = animal[0].upper()
    if firstLetter not in processedLetters:
        animalfile = open('animals-by-letter/' + firstLetter, "w+")
        animalfile.write('')
        animalfile.close()
        processedLetters.append(firstLetter)
    animalfile = open('animals-by-letter/' + firstLetter, "a+")
    animalfile.write(animal + "\t")
    animalfile.close()
