import csv
import copy
import json
import statistics
import random
import sys
from pprint import pprint
from knowledge import Knowledge
from wordlistparser import get_word_list

lang = 'en'
if len(sys.argv) >= 4:
    lang = sys.argv[3]
    
get_word_list(lang) # updates the information for the chosen language

f = open("banco-palavras.txt", "r");
words_initial = []
for word in f:
    words_initial.append(word[:-1].lower())
f.close()

frequencies = {}
with open('frequencies.json') as f: 
    frequencies = json.load(f)

letter_frequency = {}
with open('letter-frequency.csv', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for idx, row in enumerate(csv_reader):
        if idx == 0: continue

        letter = row[0].lower()
        freq = float(row[1][:-1])
        letter_frequency[letter] = freq


words = words_initial
alphabet = 'abcdefghijklmnopqrstuvxwyz'

def word_score(word: str) -> int: # FUNCTION THAT CHOOSES A WORD TO GUESS EACH TIME
    if word in frequencies.keys():
        return -frequencies[word]     # more frequent words first 
    else:
        return 0

def word_score_2(word: str) -> int: # calcula score com base na frequencia das letras usadas, priorizando maximo de letras diferentes tbm
    letters = set(word)
    score = 0
    for l in word:
        score += letter_frequency[l]

    return -(score) 

def generate_response(answer: str, guess: str): # simulates user input for automatic testing
    response = ""
    for pos in range(5):
        if guess[pos] == answer[pos]:
            response += "G"
        elif guess[pos] in answer:
            response += "Y"
        else:
            response += "B"

    return response


def play(num_of_instances:int = 1):
    tries = 0
    instances = [Knowledge(id, words, word_score) for id in range(num_of_instances)]
    curr_instance = 0

    while(curr_instance < num_of_instances):

        while not instances[curr_instance].solved: 
            
            guess = instances[curr_instance].get_guess()
            print(f"GUESS FOR WORD {curr_instance+1}: {guess}")
            for i in range(num_of_instances):
                if instances[i].solved: continue
                response = input(f"Input response for word {i+1} (G, Y, B): ").strip().upper()
                instances[i].add_hint(guess, response)
    
        curr_instance += 1
    return tries

def test(answer: str, num_of_instances:int = 1):
    tries = 0
    instances = [Knowledge(id, words, word_score) for id in range(num_of_instances)]
    curr_instance = 0

    while(curr_instance < num_of_instances):

        while not instances[curr_instance].solved: 
            
            guess = instances[curr_instance].get_guess()
            tries += 1

            for i in range(num_of_instances):
                if instances[i].solved: continue
                response = generate_response(answer, guess)
                instances[i].add_hint(guess, response)
    
        curr_instance += 1
    
    return tries

if __name__ == '__main__':

    if sys.argv[1] == 'play':
        if len(sys.argv) >= 3:
            play(int(sys.argv[2]))
        else:    
            play()

    elif sys.argv[1] == 'test':
        tries = []
        wins = 0
        games = 1000
        divs = 50
        loading_bar = "."*50

        for i in range(games):
            answer = random.choice(words)

            num_tries = test(answer)
            if num_tries <= 6: wins += 1
            tries.append(num_tries)  

            # prints loading bar
            if i%(games//divs) == 0: 
                pos = i//(games//divs)
                loading_bar = loading_bar[:pos] + '#' + loading_bar[pos+1:]
                print(f'{loading_bar} {pos*100/divs}%')


            
        print(f'Max: {max(tries)}')
        print(f'Min: {min(tries)}')
        print(f'Average: {statistics.mean(tries)}')
        print(f'Median: {statistics.median(tries)}')
        print(f'Wins (tries <= 6): {wins}/{games} ({100*wins/games}%)')
