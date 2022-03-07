import pandas as pd
from src.main.python.service.__init__ import initTXT,createResult,toNumeric,createDiasEstoqueDisponivel

def __test__():
    __main__()

def __main__():
    testReadTXT()
    testCreateResult()
    testToNumeric()
    testCreateDiasEstoqueDisponivel()

#Criação dos valores esperados de saida nos testes
df_estoque = pd.DataFrame(data={'codigo_produto': [1, 2, 3],
                                'quantidade_em_estoque': [10, 20, 30]})

df_cadastro = pd.DataFrame(data={'codigo_produto': [1, 2, 3],
                                 'descricao_produto': ['produto teste 1', 'produto teste 2', 'produto teste 3']})

df_vendas = pd.DataFrame(data={'codigo_produto': [1, 2, 3],
                               'valor_produto': [3.01, 3.02, 3.03],
                               'quantidade_vendida': [1, 4, 9],
                               'quantidade_vendida_media': [1, 2, 3]})

df_saida = pd.DataFrame(data={'codigo_produto': [1, 2, 3],'valor_produto': [3.01, 3.02, 3.03],'quantidade_vendida': [1, 4, 9],
                              'quantidade_vendida_media': [1, 2, 3],'quantidade_em_estoque': [10, 20, 30],
                              'descricao_produto': ['produto teste 1', 'produto teste 2', 'produto teste 3']})
df_saida_dias = pd.DataFrame(data={'codigo_produto': [1, 2, 3],'valor_produto': [3.01, 3.02, 3.03],'quantidade_vendida': [1, 4, 9],
                              'quantidade_vendida_media': [1, 2, 3],'quantidade_em_estoque': [10, 20, 30],
                              'descricao_produto': ['produto teste 1', 'produto teste 2', 'produto teste 3'],'dias_de_estoque_disponivel' : [10.0, 10.0, 10.0]})
def testReadTXT():
    #Lendo os arquivos de testes e
    pd.testing.assert_frame_equal(initTXT('./testes_files/entrada/', 'estoque_teste.txt', ';', 1).
                                  reset_index(drop=True),df_estoque)

    pd.testing.assert_frame_equal(initTXT('./testes_files/entrada/', 'cadastro_teste.txt', ';', 2).
                                  reset_index(drop=True),df_cadastro)

    pd.testing.assert_frame_equal(initTXT('./testes_files/entrada/', 'vendas_teste.txt', ';', 3).reset_index(),df_vendas)


def testCreateResult():
    pd.testing.assert_frame_equal(createResult(df_estoque,df_cadastro,df_vendas),df_saida)

def testToNumeric():
    pd.testing.assert_frame_equal(toNumeric(df_saida),df_saida)

def testCreateDiasEstoqueDisponivel():
    pd.testing.assert_frame_equal(createDiasEstoqueDisponivel(df_saida),df_saida_dias)