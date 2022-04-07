# MinMax com poda alpha-beta

Da mesma forma que limitamos a profundidade da árvore de busca, podemos limitar (podar, cortar) alguns dos ramos laterais da árvore de busca. Cortamos alguns ramos que não valem a pena serem percorridos. Por exemplo, considere o início da busca para o exemplo que estamos utilizando [neste material](parte5.md): 

<figure>
    <img src="../img/alpha_beta/tree1.png" /> 
</figure>

Quando o algoritmo MinMax chega no nodo de valor +1, em tese ele não precisa mais percorrer os demais nodos filhos de +1 pois já sabemos que o 0 será o valor selecionado:

<figure>
    <img src="../img/alpha_beta/tree2.png" /> 
</figure>

O mesmo acontece no ramo "B": 

<figure>
    <img src="../img/alpha_beta/tree3.png" /> 
</figure>

E no final temos uma árvore de busca com pequenas podas ao longo da busca: 

<figure>
    <img src="../img/alpha_beta/tree4.png" /> 
</figure>

Isto é possível se utilizarmos delimitadores $\alpha$ e $\beta$ nas funções $min$ e $max$ que definem os limites superiores e inferiores durante a busca: 

````python
def max_value(estado, alpha, beta, p):
    if p == 0:
        return estado.eval()
    for s in estado.sucessores():
        alpha = MAX(alpha, min_value(s, alpha, beta, p-1))
        if alpha >= beta:
            return alpha #cutoff
    return alpha
````

````python
def min_value(estado, alpha, beta, p):
    if p == 0:
        return estado.eval()
    for s in estado.sucessores():
        beta = MIN(beta, max_value(s, alpha, beta, p-1))
        if beta <= alpha:
            return beta #cutoff
    return beta
````

A chamada para este procedimento deve ser feita da seguinte forma:

````python
max_value(estado, -math.inf, math.inf, p)
````

## Uma sequência um pouco diferente para o mesmo exemplo

Talvez o exemplo apresentado acima não ilustra tão bem o impacto gerado pela versão MinMax-alpha-beta na redução do tamanho da árvore. Mas, se mudarmos um pouco a ordem de como as ações são executadas? Ao invés de gerar os sucessores seguindo a ordem A-B-C, e se gerarmos os sucessores seguindo a ordem A-C-B?

<figure>
<img src="../img/alpha_beta/tree5.png" /> 
</figure>


