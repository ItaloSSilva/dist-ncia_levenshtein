# dist-ncia_levenshtein

    Esse código é um exemplo de implementação da distância de Levenshtein em Python, que calcula a distância entre duas strings str1 e str2. 
    Vou explicar o passo-a-passo de como o código é utilizado, o que ele faz e como pode ser usado:

    Definição da Função distancia_levenshtein:
    
        A função distancia_levenshtein é definida para calcular a distância de Levenshtein entre duas strings.
        Ela recebe dois parâmetros, s1 e s2, que representam as duas strings que você deseja comparar.

    Obtendo os Comprimentos das Strings:
    
        A função começa obtendo os comprimentos das duas strings, m e n, usando a função len(s1) e len(s2).

    Inicialização da Matriz:
    
        Uma matriz chamada distancia é inicializada para armazenar os resultados intermediários dos cálculos da distância de Levenshtein.
        A matriz é bidimensional e é preenchida com zeros. Ela tem (m + 1) linhas e (n + 1) colunas. Essa matriz é a base para os cálculos.

    Preenchimento da Matriz:
    
        A matriz distancia é preenchida com valores, onde cada célula da matriz representa a distância entre partes das duas strings.
        Dois loops aninhados for são usados para iterar pelas células da matriz.
        
        Os casos base são tratados:
            
            Se a primeira string estiver vazia (i == 0), a distância é o comprimento da segunda string (j).
            
            Se a segunda string estiver vazia (j == 0), a distância é o comprimento da primeira string (i).
            
            Se os caracteres nas posições i-1 e j-1 forem iguais, não há distância entre eles.
            
        Caso contrário, a distância é calculada como a soma de 1 mais o mínimo entre a célula acima, a célula à esquerda e a diagonal superior esquerda.

    Retorno da Distância de Levenshtein:
    
        O valor na célula distancia[m][n] da matriz é a distância de Levenshtein final entre as duas strings.
        A função retorna esse valor.

    Entrada das Strings pelo Usuário:
    
        O código solicita que o usuário digite as duas strings que deseja comparar.
        As strings são inseridas através do método input() e armazenadas nas variáveis str1 e str2.

    Chamada da Função e Impressão do Resultado:
    
        A função distancia_levenshtein é chamada com as strings str1 e str2 como argumentos.
        A distância de Levenshtein entre as duas strings é calculada pela função e, em seguida, é impressa na tela.

    Em resumo, o código permite que o usuário insira duas strings e, em seguida, calcula e imprime a distância de Levenshtein entre essas duas strings, fornecendo uma medida da similaridade entre elas com base nas operações de inserção, exclusão e substituição de caracteres. 
    Isso pode ser útil em diversas aplicações, como correção ortográfica, comparação de palavras-chave em pesquisa de texto, sugestão de consultas de pesquisa e muito mais.
