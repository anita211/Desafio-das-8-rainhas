def tabuleiro(matriz):

    def Valida_Formato(matriz):
        rainhas = 0
        if len(matriz) != 8:
            return False
        for linha in matriz:
            if len(linha) != 8:
                return False
            rainhas += linha.count('1')
        if rainhas != 8:
            return False
        return True

    def Matriz_Transversa(matriz):
        result = [[],[],[],[],[],[],[],[]]
        for linha in matriz:
            j = 0
            for elemento in linha:
                result[j].append(elemento)
                j += 1
        for n in range(8):
            string = ''.join(map(str, result[n]))
            result[n] = string
        return result

    def Encontra_Rainhas(matriz):
        result = []
        for linha in matriz:
            result.append((matriz.index(linha), linha.index('1')))
        return result

    def Diagonais(lista):
        d = []
        for rainha in lista:
            linha = rainha[0]
            coluna = rainha[1]
            
            i,j = linha, coluna
            while 0 <= i <= 7 and 0 <= j <= 7:
                if (i,j) != (linha,coluna):
                    d.append((i,j))
                i+=1
                j+=1
            i,j = linha, coluna
            while 0 <= i <= 7 and 0 <= j <= 7:
                if (i,j) != (linha,coluna):
                    d.append((i,j))
                i-=1
                j-=1
            i,j = linha, coluna
            while 0 <= i <= 7 and 0 <= j <= 7:
                if (i,j) != (linha,coluna):
                    d.append((i,j))
                i-=1
                j+=1
            i,j = linha, coluna
            while 0 <= i <= 7 and 0 <= j <= 7:
                if (i,j) != (linha,coluna):
                    d.append((i,j))
                i+=1
                j-=1
            
        return d

    if not Valida_Formato(matriz):
        return -1
    
    for linha in matriz:
        if linha.count('1') != 1:
            return 0
    
    matriz_t = Matriz_Transversa(matriz)
    
    for linha in matriz_t:
        if linha.count('1') != 1:
            return 0
    
    posicao_rainhas = Encontra_Rainhas(matriz)
    diagonais = Diagonais(posicao_rainhas)
    
    for rainha in posicao_rainhas:
        if rainha in diagonais:
            return 0

    return 1