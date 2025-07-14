'''
split com união(or)

passos:
1 - fazer a função split manualmente
2 - função deve esperar receber uma string (cadeia pertencente ao alfabeto) e os parâmetros da união
3 - implementar a lógica do "ou", se a entrada for (teste ou testando), deverá:
    buscar por teste e fazer o split;
    buscar por testando e fazer o split;
    buscar por testetestando e fazer o split.
4 - input deve estar no formato XXXX|XXXX|XXXX|...
'''

def split(cadeia, separador):
    cadeia += "\0"
    cadeiaSplit = []
    cont = 0
    aux = ""
    tamanhoSeparador = 0
    if len(separador) > 1:
        tamanhoSeparador = len(separador)

    while cont != len(cadeia):
        letra = cadeia[cont]

        if tamanhoSeparador == 0 and letra != separador and letra != "\0":
            aux += letra 
        elif tamanhoSeparador != 0:
            
            if letra != separador[0] and letra != "\0":
                aux += letra
                    
            else:
                '''
                verificar se os proximos tamanhoSeparador caracteres a partir desta letra são iguais ao separador
                se forem, realizar o append na cadeiaSplit
                se n forem, continuar adicionando a letra no aux
                '''
                possivelSeparador = cadeia[cont:cont+tamanhoSeparador]
                
                if possivelSeparador == separador:

                    if aux != "":
                        if not aux.__contains__(separador):
                            cadeiaSplit.append(aux)
                        aux = ""
                        cont += tamanhoSeparador - 1
                    else:
                        aux = ""
                        cadeiaSplit.append(aux)
                        cont += tamanhoSeparador - 1
                else:
                    if letra != "\0":
                        aux += letra
                    else:
                        if aux.__contains__(separador):
                            aux = ""
                        cadeiaSplit.append(aux)
                    
        else:
            if aux != "":
                cadeiaSplit.append(aux)
                aux = ""
        
        cont += 1
    
    return cadeiaSplit

def split_com_uniao(cadeia, uniao):
    resultados = [cadeia]
    uniao = split(uniao, "|")

    for separador in uniao:
        novos_resultados = []
        for pedaco in resultados:
            partes = split(pedaco, separador)
            for p in partes:
                novos_resultados.append(p.strip())
        resultados = novos_resultados

    return resultados


texto = "maçã cama banana anjo laranja anjoteste teste uva"
print(split_com_uniao(texto, "cama|anjo|teste"))

#print(splitComUniao("O céu está azul e tranquilo, perfeito para um novo começo.", "AAA||||||azul|para|teste|$$&|tese||||a"))
#print(split("azultdtesetese teste", "tese"))# acontece problema aqui quando ocorre duas ocorrencias do mesmo separador ex: tesetese
#print(split("azul|tese|teste|tese|tese|testee", "tese"))
