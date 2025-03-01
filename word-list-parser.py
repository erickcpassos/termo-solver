from unidecode import unidecode
import csv
from pprint import pprint
import json

word_bank = "dicio.txt" 
freq_bank = "data.txt"

f = open(word_bank, "r", encoding='utf-8')
possible_words = []

for word in f:
    word = unidecode(word[:-1].lower())
    if len(word) != 5: continue
    possible_words.append(word)


f.close()

f = open("banco-palavras.txt", "w", encoding='utf-8')
for word in possible_words:
    f.write(word + "\n")

f.close()

frequencies = {}

with open(freq_bank, encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for idx, row in enumerate(csv_reader):
        if idx == 0: continue

        word = unidecode(row[0].lower())
        if len(word) != 5: continue
        frequencies[word] = int(row[1])

with open('frequencies.json', 'w') as f:
    json.dump(frequencies, f)

       

