import urllib2
import itertools
import json
import time
import sys

from itertools import product
from string import ascii_lowercase
lettercombos = [''.join(i) for i in product(ascii_lowercase, repeat = 2)]

adjectiveFile = open('adjectives', "w+")
adjectiveFile.write('')
adjectiveFile.close()

count = 1
totalAdjectives = 0

for combo in lettercombos:
    time.sleep(1)
    response = urllib2.urlopen('https://api.datamuse.com/words?sp=' + combo + '*&max=1000&md=p')
    content = response.read()
    contentDict = json.loads(content)
    adjectiveFile = open('adjectives', "a+")
    numAdjectives = 0
    for element in contentDict:
        if 'tags' in element:
            if 'adj' in element['tags']:
                if element['score'] > 40:
                    adjectiveFile.write(element['word'] + '\n')
                    numAdjectives += 1
    totalAdjectives += numAdjectives
    adjectiveFile.close()
    sys.stdout.write("\r{}/{} {}:\t{} adjectives found\t{} total".format(count, len(lettercombos), combo, numAdjectives, totalAdjectives))
    sys.stdout.flush()
    count += 1
