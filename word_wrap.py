#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys


def wordwrap_dp(words, word_wrap_column):
    # matriz de custo
    cost = [[0 for x in range(len(words))] for x in range(len(words))]

    # os próximos dois loops calcula os custos da palavras na linha
    for i in range(0, len(words)):
        cost[i][i] = word_wrap_column - len(words[i])
        for j in range(i + 1, len(words)):
            cost[i][j] = cost[i][j - 1] - len(words[j]) - 1

    for i in range(0, len(words)):
        for j in range(i, len(words)):
            if cost[i][j] < 0:
                cost[i][j] = float("inf")
            else:
                cost[i][j] = cost[i][j] ** 2

    # verifica qual é o menor custo e a sequencia de palavras
    # que atende este custo
    minCost = [0 for x in range(len(words))]
    result = [0 for x in range(len(words))]
    for i in range(len(words) - 1, -1, -1):
        minCost[i] = cost[i][len(words) - 1]
        result[i] = len(words)
        for j in range(len(words) - 1, i, -1):
            if cost[i][j - 1] == float("inf"):
                continue

            if(minCost[i] > minCost[j] + cost[i][j - 1]):
                minCost[i] = minCost[j] + cost[i][j - 1]
                result[i] = j

    # imprime as palavras
    final = ""
    i = 0
    while True:
        j = result[i]
        for k in range(i, j):
            final = final + words[k] + " "
        final = final + "\n"
        i = j
        if j >= len(words):
            break
    sys.stdout.write(final)
