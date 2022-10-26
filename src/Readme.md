# Competição de Liga4 - Documentação

### 1. Que algoritmo deve ser utilizado para desenvolver um agente jogador de Connect4 PopOut vencedor? Deve-se utilizar uma implementação de Min-Max com poda alpha-beta? Se sim, qual a profundidade que deverá ser utilizada para evitar processamentos superiores a 10 segundos por jogada? Qual a função de utilidade que deve ser utilizada?


Para um agente vencedor de Connect4 PopOut, é possível utilizar o algoritmo Min-Max. O ideal é tentar atingir a maior profundidade possível mas, com o limite de tempo de 10 segundos, uma profundidade muito grande se torna inviável. Considerando que um jogo com PopOut é mais complexo, profundidades altas se tornam ainda mais dificeis de serem alcançadas em tempos curtos. 


Para a otimização de nosso algoritmo, implementamos uma função de utilidade, em que foi considerada uma priorização de movimentos. Esta está descrita abaixo - Considerando uma ordem decrescente de recompensa:

* **Maior pontuação:** 3 do agente com um vazio do lado (vitória a um movimento)
* **Segunda maior pontuação:** 3 do agente com uma peça do outro player ao lado (podendo no futuro ser uma vitória a um movimento por conta da função pop)
* **Terceira maior pontuação (empatado):** 2 do agente com 2 vazias ao lado (vitória a 2 movimentos)
* **Terceira maior pontuação (empatado):** 2 do agente com pelo menos 1 espaço vazio e outro do oponente (vitória a 2 movimentos com a função pop)
* **Quarta maior pontuação:** 2 do agente com 2 do oponente ao lado (vitória a 2 movimentos com a função pop)
* Além disso, atribuímos **pontuações negativas**, na mesma ordem acima, para os casos espelhados - isto é, aqueles que o adversário tem a vantagem no número de peças, receberá uma pontuação mais negativa 
* Por fim, adicionalmente às posições relativas ao adversário, foram considerados pontos extras para peças colocadas na região central do tabuleiro, dado que estas tem maiores possibilidades de montar jogos.


Além disso, foi implementado um algorítmo de poda Alpha-beta para alcançar uma profundidade ainda maior. Sem esta, os 10s de tempo de processamento não eram alcançados nem com nível 4 de profundidade da árvore.


Empiricamente, foi determinado que os membros do grupo conseguiam vencer o algoritmo com profundidade 4 em algumas partidas. Com a profundidade = 5, essa tarefa já era bem mais difícil, se tornando impossível com as profundidades de 6 e 7. Mesmo assim, observamos que uma profundidade > 5 poderia ultrapassar 10s em pelo menos 15% dos jogos (alcançando no máximo 14s em 6 camadas e 36s com 7), dessa forma, optamos por manter a profundidade = 5. 


O grupo pensou em mecanismos variados para conseguir aumentar a performance de processamento do algoritmo, assim podendo chegar à camadas mais distantes da árvore:
* A primeira metodologia discutida foi em substituir as posições do tabuleiro por bits. Nesse mecanismo, cada bit representaria uma posição no tabuleiro de Connect4. A implementação de tal solução seria bastante árdua, assim como as mudanças necessárias no código já desenvolvido pelo grupo. Por fim, um código cujas posições são ditadas por bits, seria muito propenso à erros que, por sua vez, seriam muito difíceis de serem encontrados.
* A segunda discussão girou em torno de eliminar o processamento da função de pop após o 3 nível da árvore. Essa opção consideramos seriamente utilizar para deixar o algoritmo mais ágil de rodar. Mesmo assim, observamos empiricamente que, por mais que diminuísse a frequência de ocorrencias de tempos > 10s, não fazia tanta diferença no tempo máximo alcançado. Dessa forma, continuamos considerando que o risco de ultrapassar os 10s não compensava pela perda de performance que o algoritmo poderia ter ao eliminar a função pop.


### 2. O seu jogador faz uso de alguma base de conhecimento? Se sim, como ela é utilizada durante o processo de tomada de decisão?


Assim como as duas potenciais soluções descritas na questão anterior, utilizar uma base de conhecimento poderia ser utilizada para atingir uma maior profundidade da árvore. O jogador autonomo implementado não faz uso de nenhuma base, porém uma futura iteração poderia utilizá-la para poupar tempo de processamento de situações comuns. Com esse tempo poupado utilizar para aumentar a profundidade do algoritmo utilizado, dessa forma, expandindo o quanto é possível enxergar de futuras rodadas. Uma dificuldade que encontramos foi como viabilizar essa construção da base de conhecimento. Pensamos em 2 principais problemas.


* Tendo o agente jogando contra ele mesmo, o resultado da partida seria majoritariamente o mesmo (ou sempre muito similar), não conseguindo construir uma base efetiva.
* Jogando contra um jogador randômico muitas iterações deveriam ser feitas para conseguir movimentos efetivos que um outro jogador inteligente de fato faria.
* Se os membros do grupo jogassem diversas partidas contra a inteligência artificial, muito tempo seria demandado e alguns cenários poderiam ser facilmente deixados de fora


No prazo da atividade não encontramos nenhuma solução eficiente para esses problemas, dessa forma, optamos por não implementar nenhuma base de conhecimento

### 3. Qual a sua expectativa com relação ao desempenho do seu agente? Você acredita que ele irá desempenhar bem na competição? Por que? Você executou testes contra outros jogadores? Qual foram os resultados?


É esperado um alto desempenho do nosso agente no torneio. Essa expectativa é resultado de uma boa avaliação da função de Evaluate tornando as pontuações dos possíveis tabuleiros precisas em relação a situação em que se encontram e além disso para aumentar a profundidade foram feitas otimizações no código e também é utilizado o método de poda alpha-beta.


Adicionalmente, foi executado testes contra o jogador random, contra todos os integrantes do grupo e o agente fbarth, sem implementação do popout, e em todas essas disputas o nosso agente foi vitorioso.


Por fim, mesmo não tendo uma profundidade tão grande, o grupo acredita ter algumas funcionalidades que podem ser diferencias em um ambiente competitivo:


* A função pop não é desconsiderada em nenhum momento da árvore, dessa forma, acreditamos que ter visibilidade de uma movimentação adicional no jogo pode conferir como uma vantagem no sistema de pontuação de escolhas que o competidor pode realizar.
* Dar uma pontuação marginalmente maior para as peças que são colocadas no meio, maximizando a possibilidade de jogos que o nosso jogador pode realizar no inicio do jogo
* Também implementamos uma função que não prioriza o empate, mas somente a vitória. Nesse caso, os outros jogadores podem ter uma desvantagem, já que o empate é visto como uma derrota.


### 4. Quais foram as principais referências utilizadas para a implementação do seu jogador?

Utilizamos como referência base para a criação do nosso agente o código do agente FBARTH, em seguida implementamos em grupo as adaptações para que o jogador também realizasse e calculasse o PoPout, e alteramos a função utilidade. Além da implementação utilizamos como uma boa referência o artigo [Improving Minimax performance](https://levelup.gitconnected.com/improving-minimax-performance-fc82bc337dfd) para otimização do código minimax. Além de algumas das soluções já trazidas na Questão 1 para a otimização do nosso código, o artigo também traz diversos pontos relevantes e interessantes de se aprender para futuras implementações de AI. 

Além disso, a fim de entender mais a fundo o algoritmo de poda alpha-beta, pesquisamos diversas fontes, sendo a mais didática delas o vídeo[Algorithms Explained – minimax and alpha-beta pruning](https://www.youtube.com/watch?v=l-hh51ncgDI), também utilizando os conceitos do vídeo para melhorar a performance do nosso algoritmo.

### 5. Existem diferenças significativas entre um jogador de Connect4 e um jogador de Connect4 PopOut em termos de árvore de busca e função de avaliação? É possível utilizar o jogador implementado para o Connect4 PopOut em competições de Connect4 sem muitas modificações? 

Sim, existem diferenças significativas entre um jogador de Connect4 e um jogador de Connect4 PopOut. Na Árvore de busca é possível gerar mais de caminhos para a tomada de decisão, no caso médio onde um jogador tenha 3 peças na primeira linha, em cada árvore será gerada mais 3 filhos.Veja no exemplo a diferença de filhos em um caso simples:

![Image](/Users/gustavosteinbergberger/Desktop)

A próxima jogada é do jogador círculo, nessa próxima jogada em um connect4 comum há 7 possibilidades, enquanto que no connect4 há 10 possibilidades. um aumento de quase 50% na quantidade de filhos.


Além de aumentar significativamente a quantidade de ramos da árvore de decisão, a função de avaliação é alterada também, visto que agora é vantajoso possuir peças em cima da sua ou do oponente em casos que suas peças estejam na linha de baixo horizontalmente e diagonalmente.


Para considerar casos mais benéficos em uma partida com popout, atribuímos uma pontuação que não existe em um jogo sem popout, em casos com peças juntas, com peças do oponente também, já que uma situação como essa pode ser decisiva incluindo pops.


Para esse jogador de popout jogar uma partida normal, a função eval precisa ser modificada considerando as particularidades dos casos benéficos desse tipo de partida. Além disso, seria necessário remover as opções de pop da árvore do agente.
