def tabuleiro(matriz):

    def Valida_Formato(matriz):
        if len(matriz) != 8:
            return False
        for linha in matriz:
            if len(linha) != 8:
                return False
        return True

    if not Valida_Formato(matriz):
        return -1
    
    for linha in matriz:
        if linha.count('1') != 1:
            return 0
    
    return 1