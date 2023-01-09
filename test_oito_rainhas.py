"""Module providing function for the "oito rainhas" problem."""

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

jogo_falho_diagonal = ['00000001',
               '00000010',
               '00000100',
               '00001000',
               '00010000',
               '00100000',
               '01000000',
               '10000000']

jogo_solucao = ['00001000',
               '01000000',
               '00010000',
               '00000010',
               '00100000',
               '00000001',
               '00000100',
               '10000000']

def test_jogo_invalido_tamanho():
  assert tabuleiro(jogo_invalido_tamanho)==-1

def test_jogo_invalido_linha():
  assert tabuleiro(jogo_invalido_linha)==-1

def test_jogo_invalido_numero_de_rainhas():
  assert tabuleiro(jogo_invalido_numero_de_rainhas)==-1

def test_jogo_falho_linha():
  assert tabuleiro(jogo_falho_linha)==0

def test_jogo_falho_coluna():
  assert tabuleiro(jogo_falho_coluna)==0

def test_jogo_falho_diagonal():
  assert tabuleiro(jogo_falho_diagonal)==0

def test_jogo_solucao():
  assert tabuleiro(jogo_solucao)==1
