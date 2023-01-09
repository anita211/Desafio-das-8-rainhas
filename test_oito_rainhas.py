from oito_rainhas import tabuleiro

jogo_invalido_tamanho = ['00000001',
                 '01000000',
                 '00010000',
                 '00000010',
                 '00100000',
                 '00000001',
                 '00000100']

jogo_invalido_linha = ['00000001',
               '01000000',
               '00010000',
               '00000010',
               '00100000',
               '00000001',
               '00000100',
               '1000000']

jogo_valido_posicao_falha = ['00000001',
                             '01000000',
                             '00010000',
                             '00000010',
                             '00100000',
                             '00000001',
                             '00000100',
                             '10000000']

def test_quando_tabuleiro_recebe_jogo_invalido_tamanho_deve_retornar_menos_1():
    assert tabuleiro(jogo_invalido_tamanho)==-1

def test_quando_tabuleiro_recebe_jogo_invalido_linha_deve_retornar_menos_1():
    assert tabuleiro(jogo_invalido_linha)==-1