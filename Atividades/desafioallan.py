def distancia_levenshtein(s1, s2):
   
   # Obter os comprimentos das duas strings
    m, n = len(s1), len(s2)

    # Inicializar uma matriz para armazenar os resultados
    # Matriz bidimensional que é preenchida com zeros. (m+1) linhas e (n+!) colunas
    distancia = [[0] * (n + 1) for _ in range(m + 1)]

    # Preenchendo a matriz com valores
    for i in range(m + 1):
        for j in range(n + 1):
            # Caso 1: Se a primeira string estiver vazia, a distância é o valor da segunda string
            if i == 0:
                distancia[i][j] = j

            # Caso 2: Se a segunda string estiver vazia, a distância é o valor da primeira string
            elif j == 0:
                distancia[i][j] = i

            # Se os caracteres nas posições i-1 e j-1 forem iguais, não há distância entre eles    
            elif s1[i - 1] == s2 [j - 1]:
                distancia[i][j] = distancia[i - 1][j - 1]

            # Calculamos a Inserção, Exclusão e Substituição    
            else:
                distancia[i][j] = 1 + min(distancia[i - 1][j], distancia[i][j - 1], distancia[i - 1][j - 1])

    # O valor na célula distancia[m][n] é a distância de levenshtein final das duas strings.
    return distancia[m][n]


str1 = input("Digite a primeira String \n>")
str2 = input("Digite a segunda String \n>")
print("\nA distância entre as duas Strings é de:", distancia_levenshtein(str1, str2))
