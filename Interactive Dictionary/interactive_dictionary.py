import json
import sys
from difflib import get_close_matches

f = open("data.json")
# json.load gets an object file and returns a dictionary
data = json.load(f)

def getTranslation(word):
    # data.keys() returns a list of all the keys in the dic
    # get_close_matches returns a list of all the possible words(n options) from data.keys() that match the input word
    N, CUTOFF = 4, 0.2
    matches = get_close_matches(word, data.keys(), N, CUTOFF)
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif matches:
        while matches:
            answer = input("Did you mean %s instead? if yes press Y, otherwise N: " % matches[0]).lower()
            if answer == 'y':
                return data[matches[0]]
            elif answer == 'n':
                matches.pop(0)
            else:
                return "We didn't understand your entry"
        return "No word found in the dictionary"
    else:
        return "No word found in the dictionary"

def main():
    word = input("Insert a word to translate or press Q to exit: ").lower()
    if word == 'q':
        sys.exit()
    translated_word = getTranslation(word)
    if type(translated_word) == list:
        for item in translated_word:
            print(item)
    else:
        print(translated_word)

while True:
    main()