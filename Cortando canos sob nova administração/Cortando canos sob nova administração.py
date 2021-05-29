def mochila(i,j,comprimentoValor):
    if i == 0 or j == 0:
        return 0
    else:
        t = []

        for linha in range(i+1):
            t.append([])
            for coluna in range(j + 1):
                if linha == 0 or coluna == 0:
                    t[linha].append(0)
                else:
                    if comprimentoValor[linha-1][0] > coluna:
                        t[linha].append(t[linha-1][coluna])
                    else:
                        resultado = defineMaximo(t[linha-1][coluna], t[linha-1][coluna-comprimentoValor[linha-1][0]] + comprimentoValor[linha-1][1])

                        if resultado > 0 and resultado >= t[linha-1][coluna]:
                            t[linha].append(0)
                            corte_de_cano = coluna
                            valor_cano = 0
                            while corte_de_cano >= comprimentoValor[linha-1][0]:
                                corte_de_cano -= comprimentoValor[linha-1][0]
                                valor_cano += comprimentoValor[linha-1][1]
                            t[linha][coluna] = defineMaximo(valor_cano, t[linha-1][coluna])
                        else:
                            t[linha].append(resultado)

    return t[i][j]

def defineMaximo(termoA, termoB):

    if termoA > termoB:
        return termoA
    else:
        return termoB




numero, tamanhoMaximo = [int(e) for e in input().split()]
comprimentoValor = []
for e in range(numero):
    pedido = tuple(map(int, input().split()))
    comprimentoValor.append(pedido)

print(mochila(numero,tamanhoMaximo,comprimentoValor))



