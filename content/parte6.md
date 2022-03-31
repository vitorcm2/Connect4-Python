# Algoritmo Min-Max (parte 2)

??? question "E se limitarmos a busca até uma determinada profundidade $p$?"

    Por exemplo, no caso abaixo em $p=2$?

    <figure>
        <img src="../img/min-max-search-com-limite.png" /> 
    </figure>

    O que está faltando?

??? note "Função de utilidade"

    * A ideia é substituir a avaliação de estados terminais pela avaliação de estados intermediários. 

    * A função de avaliação deve retornar um valor alto para estados que tem uma utilidade maior para o nosso robô e valores baixos para estados que tem um utilidade menor. 

    * Podemos utilizar as mesmas regras vistas em [Definindo algumas verificações](parte3.md). 

??? note "Versão Min-Max com limite de profundidade"

    ````python
    def max_value(estado, p):
        if p == 0:
            return estado.eval()
        v = -99999
        for s in estado.sucessores():
            v = MAX(v, min_value(s, p-1))
        return v
    ````

    ````python
    def min_value(estado, p):
        if p == 0:
            return estado.eval()
        v = 99999
        for s in estado.sucessores():
            v = MIN(v, max_value(s, p-1))
        return v
    ````

??? warning "Humano versus Min-Max com limite de profundidade" 

    Vamos testar o desempenho de um Min-Max com profundidade 1, 3, 5 e 7? Digite: 

    ````bash
    python connect4_with_ai.py minmax 1

    python connect4_with_ai.py minmax 3

    python connect4_with_ai.py minmax 5

    python connect4_with_ai.py minmax 7
    ````

??? question "Quais foram as diferenças observadas?"

    * Teve alguma diferença em termos de tempo de processamento?
    * Teve alguma diferença em termos de desempenho? 
    * Alguma das configurações chega a ter um desempenho similar ao de um humano?

