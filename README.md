# Termo Solver

Esse script em Python é um assistente para encontrar a palavra secreta do jogo Termo.

O programa te sugere palavras a serem inseridas no jogo e recebe as dicas sobre a posição das letras. Sua eficácia depende do banco de palavras, mas, em média, o programa utiliza 5.03 tentativas e vence o jogo em 86% das vezes.

Para usar o solver, basta rodar o arquivo main.py com o argumento play:

```
$ py main.py play
```

O programa sugerirá uma palavra que você deverá inserir no Termo. Então, insira no programa as dicas obtidas no jogo. Isso é feito no formato de uma string de 5 caracteres como "BGGYB" ou a string "N":

* "B" significa uma casa preta (letra não existe na palavra)
* "Y" significa uma casa amarela "letra na posição incorreta" e
* "G" significa uma casa verde (letra na posição correta).
* Em alguns casos, a palavra sugerida pelo programa pode não ser aceita no jogo. Nesse caso, responda com "N" para que o programa sugira uma nova palavra.
* Ao fim, quando o programa acertar a palavra, insira "GGGGG" para terminá-lo (ao invés de fechar o terminal, pois o solver fica feliz em saber que acertou).

O banco de palavras considerado pelo programa é o arquivo banco-palavras.txt. Caso queira alterá-lo, basta rodar o arquivo word-list-parser.py, alterando a variável 'word_bank' para o caminho do arquivo .txt desejado.

O arquivo main.py também permite que o jogo simule várias partidas contra si mesmo para avaliar sua performance. O banco de palavras considerado também é o banco-palavras.txt e o número de partidas simuladas pode ser alterado na variável 'game' na \__main__. Para rodar o modo de teste, basta utilizar o argumento 'test':

```
$ py main.py test
```

## Próximas melhorias

[] Possibilitar jogo automático interagindo com o browser
[] Aceitar input de dicas para jogos em curso
[] Funcionar para variantes como dueto e quarteto
[] Adicionar bancos de dados em inglês para jogar Wordle