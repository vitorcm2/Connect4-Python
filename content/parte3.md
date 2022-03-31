# Implementando um jogador de verdade! 

??? question "Por onde eu começo?"

    <figure>
        <img src="../img/comeco.png" width="300"/> 
    </figure>

??? question "O que eu faço agora?" 

    <figure>
    <img src="../img/comeco_1.png" width="300"/> 
    </figure>

??? question "E agora?" 

    <figure>
    <img src="../img/comeco_2.png" width="300"/> 
    </figure>

??? question "Qual é a melhor opção?"

    <figure>
    <img src="../img/comeco_completo.png" /> 
    </figure>

    É necessário ter uma função qualquer na implementação que diga qual é a melhor ação. Por exemplo, dizendo qual é o estado que tem **maior utilidade** para o nosso robô.  

??? tip "Definindo algumas verificações"

    * é um movimento vencedor?
    * está dominando o centro?
    * está criando oportunidades na horizontal?
    * está criando oportunidades na vertical?
    * está criando oportunidades na diagonal?

??? warning "Humanos versus um robô melhorado"

    Considerando que você já está no diretório `src`, digite:

    ````bash
    python connect4_with_ai.py flat
    ````

??? note "Humanos versus um robô melhorado" 

    Agora temos um robô melhor que o robô aleatório. No entanto, este ainda é um robô que não consegue vencer na maioria das vezes. 

    **O que podemos fazer para [melhorar o desempenho](parte4.md) do robô?**