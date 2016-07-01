# Projeto 3 - SCC-5900  – Projeto de algoritmos
O objetivo deste trabalho é implementar um algoritmo de Word Wrap que minimize a soma dos quadrados dos espaços remanescentes de cada linha, utilizando o paradigma de Programação Dinâmica, e calcular e justificar sua complexidade.


# Problema Word Wrap
Word Wrap é o nome dado à quebra automática de linhas, habitualmente realizada por programas que exibem conteúdo textual, como processadores de texto e navegadores de internet, de forma que tal conteúdo possa ser exibido em determinado espaço sem necessidade de uma barra de rolagem horizontal.


# Programação Dinâmica
Neste trabalho utilizamos a abordagem de Programação Dinâmica para resolver o Word Wrap. Ao usar esta abordagem tentamos reduzir globalmente a soma dos quadrados dos espaços remanescentes e assim tornar a leitura um pouco mais agradável.


## Função de Recorrência
No primeiro momento, computamos o custo de todas as possíveis linhas em uma matriz lc[][]. O valor de lc[i][j] indica que o custo de colocar as palavras de i até j em úm única linha onde i e j são índices das palavras de uma sequência. Se a sequência de palavras de i até j não pode ser colocada em uma única linha, então lc[i][j] é considerado infinito (para evitar de ser parte da solução). Assim que construírmos a matriz lc[][], nós podemos calcular o custo total usando a função de recursão abaixo. Na seguinte função, C[j] é custo total ótimo para as palavras de 1 até j.



![alt funcao](https://github.com/DaniloOliveira28/Word_Wrap/blob/master/Data/word_wrap.png "Histograma de Atribuições")



## Implementação

A implementação está explicada nos comentários do código. A atual implementação possui as seguintes complexidades:

    Complexidade de Tempo: O(nˆ2)

    Complexidade de Espaço: O(nˆ2)

## Conclusões
O algoritmo se mostrou uma boa solução para resolver o problema proposto, porém é possível reduzir a complexidade de espaço para O(n)

# Como usar?
    Usage: main.py -l [1-inf]
        "-l : número máximo de colunas"


# Referências
[1] http://www.geeksforgeeks.org/dynamic-programming-set-18-word-wrap/

[2] https://en.wikipedia.org/wiki/Line_wrap_and_word_wrap

[3] https://www.youtube.com/watch?v=RORuwHiblPc
