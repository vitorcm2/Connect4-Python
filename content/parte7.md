# Máquina contra Máquina

??? question "Será que um jogador com min-max pode perder de um jogador aleatório?"

    Que tal testarmos?

    ````bash
    python connect4_ai_versus_ai.py random 0 minmax 5
    ````

    Neste caso o primeiro jogador é o aleatório. 

    E se usarmos um minmax com profundidade igual a 1?

    ````bash
    python connect4_ai_versus_ai.py random 0 minmax 1
    ````


??? question "E se jogarmos min-max contra min-max?"

    Com profundidades iguais:

    ````bash
    python connect4_ai_versus_ai.py minmax 5 minmax 5
    ````

    Com profundidades diferentes:

    ````bash
    python connect4_ai_versus_ai.py minmax 1 minmax 5
    ````

??? question "Questões gerais"

    * Será que uma pessoa pode aperfeiçoar o seu conhecimento sobre Liga4 jogando contra máquinas?

    * Será que uma pessoa pode aperfeiçoar o seu conhecimento sobre Liga4 estudando partidas feitas por duas máquinas?

    * Será que é possível uma máquina aprender a jogar Liga4 jogando contra uma outra máquina que sabe Liga4?
