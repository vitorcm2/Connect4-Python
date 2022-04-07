# Algoritmo Min-Max (parte 1)

??? note "Árvore de busca"

    <figure>
        <img src="../img/arvore_busca.png" /> 
    </figure>

??? note "Um exemplo de busca na árvore min-max" 

    <figure>
        <img src="../img/min-max-search-1.png" /> 
    </figure>

??? note "Um exemplo de busca na árvore min-max (parte 2)" 

    <figure>
        <img src="../img/min-max-search-2.png" /> 
    </figure>

??? question "Qual ação o robô deve escolher?"

    **C** - aquela que maximiza o seu ganho. 

??? note "Como implementar o Min-Max"

    ````python
    def max_value(estado):
        if estado.eh_final():
            return estado.eval()
        v = -math.inf
        for s in estado.sucessores():
            v = MAX(v, min_value(s))
        return v
    ````

    ````python
    def min_value(estado):
        if estado.eh_final():
            return estado.eval()
        v = math.inf
        for s in estado.sucessores():
            v = MIN(v, max_value(s))
        return v
    ````

??? question "Agora temos um robô vencedor? Vamos testar?" 

    Considerando que você já está no diretório `src`, digite:

    ````bash
    python connect4_with_ai.py complete
    ````

    E ai? **O que está acontecendo?**

??? warning "Tamanho da árvore de busca"

    * Talvez o tamanho da árvore de busca seja muito grande para o robô procurar até todos os estados finais. 

    * ramificação - quantidade de possíveis ações em cada estado ($b$) = 6

    * profundidade da solução ($d$): $6 \times 7 = 42$. 

    * tamanho da árvore: 

    $\mathcal{O}(b^{d}) = b^{0} + b^{1} + b^{2} + \cdots + b^{d}$

    $\mathcal{O}(b^{d}) = 6^{0} + 6^{1} + b^{2} + \cdots + b^{42}$ 

    $\mathcal{O}(b^{d}) = 6^{0} + 6^{1} + b^{2} + \cdots + 6^{42}$

    $\equiv 1 + 6 + 36 + \cdots + 4.812298\mathrm{e}{+32}$

??? question "Será que precisamos explorar a árvore inteira?"

    [Próxima etapa](parte6.md)