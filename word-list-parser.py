from unidecode import unidecode

word_bank = "dicio.txt" 

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