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

    if not Valida_Formato(matriz):
        return -1
    
    for linha in matriz:
        if linha.count('1') != 1:
            return 0
    
    matriz_t = Matriz_Transversa(matriz)
    
    for linha in matriz_t:
        if linha.count('1') != 1:
            return 0
    
    return 1