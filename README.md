# Connect4-Python

Connect 4 programmed in python using pygame.

## Why I forked this project?

Because I would like an user interface for my agents that know how to play Connect-4. 

## Running

````bash
python3 -m virtualenv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
````

The game is started by running `src/connect4.py` or `src/connect4_with_ai.py`. 

* `src/connect4.py`: dois jogadores jogando de forma manual.
* `src/connect4_with_ai.py`: um jogador manual e outro artificial.
* `python connect4_with_ai.py random`: o jogador artificial tem comportamento aleatório.
* `python connect4_with_ai.py minmax 5`: o jogador artificial implementa o algoritmo min-max. O número informado é a profundidade que o algoritmo min-max irá considerar - precisa ser um valor maior ou igual a 1.

* `python connect4_ai_versus_ai.py random 0 minmax 5`: o primeiro argumento define o primeiro jogador. Se for `random` então o segundo argumento pode ser qualquer valor. O terceiro argumento define o segundo jogador. Se o jogador for `minmax` então o argumento subsequente sempre precisa ser a profundidade adotada pelo `minmax`. 