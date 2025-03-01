import copy
import statistics
import random
from pprint import pprint

f = open("banco-palavras.txt", "r");

words_initial = []
for word in f:
    words_initial.append(word[:-1].lower())

f.close()

words = words_initial

alphabet = 'abcdefghijklmnopqrstuvxwyz'

initial_space_knowledge = {}
for c in alphabet:
    initial_space_knowledge[c] = True

knowledge = [copy.deepcopy(initial_space_knowledge) for i in range(5)]

needed_letters = set()

def reset_knowledge():
    global knowledge
    global needed_letters
    global words

    knowledge = [copy.deepcopy(initial_space_knowledge) for i in range(5)]
    needed_letters = set()
    words = copy.deepcopy(words_initial)

def is_coherent(word: str) -> bool: 
    for letter in needed_letters:
        if letter not in word: return False
    
    for pos in range(5):
        letter_in_pos = word[pos]
        if not knowledge[pos][letter_in_pos]:
            return False

    return True

def generate_response(answer, guess):
    response = ""
    for pos in range(5):
        if guess[pos] == answer[pos]:
            response += "G"
        elif guess[pos] in answer:
            response += "Y"
        else:
            response += "B"

    return response


def play(answer):
    tries = 0
    while(True):
        # pprint(needed_letters)
        # pprint(knowledge)
        
        global words
        #words_updated = copy.deepcopy(words) # this list will be used as words array in next iteration. it removes words already incoherent

        tries += 1
        random.shuffle(words)

        guess = "ERRO"

        # print(f"palavra na lista? {answer in words}")
        # print(f"palavra ta coerente? {is_coherent(answer)}")
        for word in words:
            # if word == answer:
                # print("PASSEI PELA RESPOSTA AQUI")
            
            if is_coherent(word):
                guess = word
                break
            else:
                if word == answer: print(f"removed {word}")
                #words_updated.remove(word) # removes incoherent words from word list. apparently, not necessarily faster

        #words = copy.deepcopy(words_updated)
        
        if(guess == "ERRO"):
            #pprint(words)
            print("NO MORE GUESSES")
            break

        # print(guess)

        response = ""
        while len(response) != 5 and response != "N": 
            #response = input("Input response (G, Y, B): ")
            response = generate_response(answer, guess)
            # print(response)


        if response == "N":
            words.remove(guess)
            continue

        if response == "GGGGG": break

        for pos, val in enumerate(response):
            if val == "G" or val == "Y":
                needed_letters.add(guess[pos])

        for pos, val in enumerate(response):
            if val == "B":
                if guess[pos] in needed_letters:
                    knowledge[pos][guess[pos]] = False
                    continue    

                for i in range(5):
                    knowledge[i][guess[pos]] = False
            elif val == "Y":
                needed_letters.add(guess[pos])
                knowledge[pos][guess[pos]] = False
            else:
                needed_letters.add(guess[pos])
                for lett in alphabet:
                    if lett != guess[pos]: knowledge[pos][lett] = False
                    else: knowledge[pos][guess[pos]] = True
    
    return tries

if __name__ == '__main__':
    tries = []
    wins = 0
    games = 1000
    divs = 50
    loading_bar = "."*50
    for i in range(games):
        reset_knowledge()
        answer = random.choice(words)
        # print(f" ==== GAME {str(i)}: {answer} ==== ")

        num_tries = play(answer)
        # print(f'\nTries: {num_tries}\n')
        if num_tries <= 6: wins += 1
        tries.append(num_tries)  
        if i%(games//divs) == 0: 
            pos = i//(games//divs)
            loading_bar = loading_bar[:pos] + '#' + loading_bar[pos+1:]
            print(f'{loading_bar} {pos*100/divs}%')


        
    print(f'Max: {max(tries)}')
    print(f'Min: {min(tries)}')
    print(f'Average: {statistics.mean(tries)}')
    print(f'Median: {statistics.median(tries)}')
    print(f'Wins (tries <= 6): {wins}/{games} ({100*wins/games}%)')
