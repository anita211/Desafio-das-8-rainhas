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

jogo_invalido_numero_de_rainhas = ['00000001',
               '01000000',
               '00010000',
               '00000010',
               '00100000',
               '00000001',
               '00000100',
               '10000001']

jogo_falho_linha = ['01001000',
               '00000000',
               '00010000',
               '00000010',
               '00100000',
               '00000001',
               '00000100',
               '10000000']

jogo_falho_coluna = ['00001000',
               '00001000',
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

def test_quando_tabuleiro_recebe_jogo_invalido_numero_de_rainhas_deve_retornar_menos_1():
    assert tabuleiro(jogo_invalido_numero_de_rainhas)==-1

def test_quando_tabuleiro_recebe_jogo_falho_linha_deve_retornar_0():
    assert tabuleiro(jogo_falho_linha)==0

def test_quando_tabuleiro_recebe_jogo_falho_coluna_deve_retornar_0():
    assert tabuleiro(jogo_falho_coluna)==0