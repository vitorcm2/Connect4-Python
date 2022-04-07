# Um pouco de história e tendências

??? note "Origens"

    * [Claude Shannon. Programming a Computer for Playing Chess. Philosophical Magazine, Ser.7, Vol. 41, No. 314 - March 1950.](https://vision.unipv.it/IA1/ProgrammingaComputerforPlayingChess.pdf) Uma proposta de uso do algoritmo Min Max no jogo de Xadrez. 

    * [Claude Shannon](https://en.wikipedia.org/wiki/Claude_Shannon) cita neste artigo o livro publicado por [John von Neumann](https://en.wikipedia.org/wiki/John_von_Neumann) e [Oskar Morgenstern](https://en.wikipedia.org/wiki/Oskar_Morgenstern): Theory of Games and Economic Behavior publicado em 1944. 

    * John von Neumann cita no seu livro as origens da ideia de Min Max: *Waldegrave (1713) Minmax solution of a 2-person, zero-sum game, reported in a letter from P. de Montmort to N. Bernouilli, transl, and with comments by H. W. Kuhin in W. J. Baurnol and Goldfeld (eds.), Precusors of Mathenatical Economics*.

??? note "Deep Blue versus Garry Kasparov" 

    <figure>
        <img src="../img/deepblue.png" /> 
    </figure>

    * O DeepBlue fazia uso do algoritmo MinMax com poda alpha-beta. 
    * A solução tinha 256 processadores dedicados para a tarefa.
    * Examinava em torno de 30 bilhões de movimentos por minuto. 
    * A profundidade geralmente era de 13. No entanto, em determinadas situações podia chegar até 30. 
    * Para fazer a poda da árvore ou alongar o caminho de busca, a solução fazia uso de uma base de jogos históricos de Xadrez. Com isto era possível determinar o valor de um estado sem continuar a busca.

    * [Game over: Kasparov and The Machine, 2003](https://www.imdb.com/title/tt0379296/)
    * [Deep Blue - Down the Rabbit Hole](https://www.youtube.com/watch?v=HwF229U2ba8): um vídeo um tanto quanto interessante sobre o assunto com vários detalhes que são difíceis de encontrar em outras fontes. 

??? question "O que mudou de Shannon até o Deep Blue?" 

    <figure>
        <img src="../img/moravec.jpg" /> 
    </figure>    

    * Imagem retirada do artigo *[When will computer hardware match the human brain?](https://jetpress.org/volume1/moravec.pdf)* de Hans Moravec de 1997. 

??? question "O avanço no jogo de xadrez parou depois do Deep Blue?" 

    <figure>
        <img src="../img/elo_rating.png" /> 
    </figure>    

    * Imagem retirada do texto *[Chess’s New Best Player Is A Fearless, Swashbuckling Algorithm](https://fivethirtyeight.com/features/chesss-new-best-player-is-a-fearless-swashbuckling-algorithm/)* publicado em 2018.

    * Elo é um ranking utilizado para medir o desempenho de jogadores em qualquer jogo de soma zero, incluindo o xadrez.

??? note "AlphaZero"

    <figure>
        <img src="../img/alphazero.png" /> 
    </figure>    

    * Imagem retirada do artigo D. Silver et al., “[Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm](http://arxiv.org/abs/1712.01815)”, CoRR, vol. abs/1712.01815, 2017, [Online]. Disponível em: http://arxiv.org/abs/1712.01815
    
    * Uma segunda versão do artigo foi publicada em D. Silver et al., “[A general reinforcement learning algorithm that masters chess, shogi, and Go through self-play](https://www.science.org/doi/10.1126/science.aar6404)”, Science, vol. 362, nº 6419, p. 1140–1144, 2018.
 

??? note "Impactos"

    * M. Sadler, N. Regan, e G. Kasparov, Game Changer: AlphaZero’s Groundbreaking Chess Strategies and the Promise of AI. New in Chess, 2019.

    * N. Tomasev, U. Paquet, D. Hassabis, e V. Kramnik, “Assessing Game Balance with AlphaZero: Exploring Alternative Rule Sets in Chess”, CoRR, vol. abs/2009.04374, 2020, [Online]. Disponível em: https://arxiv.org/abs/2009.04374

??? warning "Próximas atividades"

    Se você quiser, é possível baixar todo o código na sua máquina, configurar o ambiente e executar o jogo e os jogadores na sua máquina local. Se esta for a sua intenção então você pode ir para o arquivo de [configuração](configuracao.md).

??? warning "Material adicional"

    Existe uma variante do algoritmo MinMax chamado MinMax com alpha-beta. A descrição de como esta variante funciona pode ser acessada [aqui](alpha_beta.md).