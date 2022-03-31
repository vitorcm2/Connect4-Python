# Um pouco de história

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

    