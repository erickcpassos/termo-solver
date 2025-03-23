# Termo Solver

This Python script was built to be an assistant to find the secret word in the Brazilian game 'Termo' and other Wordle-like games.

The program suggests words to be inserted into the game and receives the hints regarding the letters' position. Its efficiency depends on the word bank, but, on average, it takes 5.03 tries and wins the game in 86% (in Termo, in Brazilian Portuguese).

To use the solver, run the file main.py with the argument play:

```
$ py main.py play [number of instances, default = 1] [language, default = en]
```

As of now, the available languages are English (en) and Brazilian Portuguese (br).

The number of instances is the name of simultaneous games (in Termo, there is the option to play more than one word at once).

For example, to play a usual Wordle game, you should run:

```
$ py main.py play 1 en   // simply 'py main.py play' would also work because of the default values
```

The program will suggest a word that you should enter in the game. Then, for each instance, enter the hints obtained back into the program. This is done either as a 5-letter string, such as "BGGYB", or as the string "N".

* "B" means a black square (the letter does not exist in the word)
* "Y" means a yellow square (the letter is in the wrong position)
* "G" means a green square (the letter is in the correct position)
* In some cases, the word suggested by the program might not be accepted in the game. In this case, answer with "N", in all instances, so that the game can suggest a new word.
* In the end, when the program finds the correct word, insert "GGGGG" to terminate it.
* In a multi-instance game, the program will try to solve them one by one.

## Next improvements

- [ ] Implement interaction with the browser to obtain hints automatically
- [ ] Improve word score calculation for English word list