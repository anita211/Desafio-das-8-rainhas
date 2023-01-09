from oito_rainhas import tabuleiro

jogo_invalido = [1]

jogo_valido_posicao_falha = ['00000001',
                             '01000000',
                             '00010000',
                             '00000010',
                             '00100000',
                             '00000001',
                             '00000100',
                             '10000000']

def test_quando_tabuleiro_recebe_jogo_invalido_deve_retornar_menos_1():
    assert tabuleiro(jogo_invalido)==-1

def test_jogo_valido_posicao_falha():
    assert tabuleiro(jogo_valido_posicao_falha)==0