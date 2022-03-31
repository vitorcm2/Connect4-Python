# Colando um robô na partida

??? info "Alterando o código"

    Na linha 114 e 115 do arquivo [connect4.py](../src/connect4.py) é possível ver o seguinte trecho de código: 

    ````python
    posx = event.pos[0]
	col = int(math.floor(posx/SQUARESIZE))
    ````

    Precisamos trocar este trecho por algo como: 

    ````python
    col = player.move(player_code, board)
    ````

    Sendo que o `player` pode ser uma instância da classe: 

    ````python
    class MeuJogador(Player):

    def name(self):
        return "Meu Jogador super simples"

    def move(self, player_code, board):
        # TODO lógica para escolher uma coluna
        return col
    ````

??? question "Como podemos implementar um jogador super simples?"

    Criando um jogador que joga de forma aleatória! 

    ````python
    from random import randint
    from Player import Player

    class RandomPlayer(Player):

        def name(self):
            return "Random"

        #
        # retorna a coluna onde a bola será jogada
        #
        def move(self, player_code, board, depth):
            return randint(0, 6)
    ````

??? warning "Humanos versus um robô super simples"

    Considerando que você já está no diretório `src`, digite:

    ````bash
    python connect4_with_ai.py random
    ````

??? question "Vamos implementar algo um pouco mais eficiente?" 

    * Que abordagens podemos utilizar para implementar um robô mais **inteligente**? 
    * O que seria uma robô mais "inteligente"?
    
??? done "Próxima etapa"

    * [Implementando um jogador que sabe jogar](parte3.md)
