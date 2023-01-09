def tabuleiro(matriz):

    def Valida_Formato(matriz):
        return True

    if not Valida_Formato(matriz):
        return -1
    
    for linha in matriz:
        if linha.count('1') != 1:
            return 0
    
    return 1