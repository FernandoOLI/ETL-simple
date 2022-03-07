import pandas as pd
import numpy as np

def __init__():
    __main__()

def __main__():
    toCSV(createDiasEstoqueDisponivel(toNumeric(createResult(initTXT('./entrada/', 'estoque.txt', ';', 1),
                                                       initTXT('./entrada/', 'cadastro.txt', ';', 2),
                                                       initTXT('./entrada/', 'vendas.txt', ';', 3)))))

def initTXT(path,filename,separator,choose):
    if choose == 1:
        return initEstoque(path,filename,separator)
    elif choose == 2:
        return initCadastro(path,filename,separator)
    elif choose == 3:
        return initVendas(path,filename,separator)
    else:
        print('Opção inválida')
        return None

def initEstoque(path,filename,separator):
    #caso o valor de estoque venha duplicado, foi considerado  o último valor inserido
    return readTXT(path,filename,separator).drop_duplicates(subset='codigo_produto', keep='last',inplace=False)

def initCadastro(path,filename,separator):
    #removendo cadastros com o mesmo id
    return readTXT(path, filename, separator).drop_duplicates(subset=['codigo_produto'])

def initVendas(path,filename,separator):
    #caso o valor de vendas venha duplicado, são removidos
    #entretando se o id for igual mas o valor diferente, ambos são considerados
    return readTXT(path, filename, separator).groupby(['codigo_produto','valor_produto']).agg(quantidade_vendida=('quantidade_vendida', 'sum'),
                                                                                              quantidade_vendida_media=('quantidade_vendida', 'mean'))

def createResult(df_estoque,df_cadastro,df_vendas):
    #Fazendo o full outer Join de cadastro com vendas e substituindo os valores nulos por zero
    #Depois o left join do resultado com cadastro, pois caso exista em cadastro e não no resultado será desconsiderado
    #
    return pd.merge(pd.merge(df_vendas, df_estoque, how='outer', on=['codigo_produto', 'codigo_produto']).fillna(0),
                    df_cadastro, how='left', on=['codigo_produto', 'codigo_produto']).fillna('Não Cadastrado')

def readTXT(path,filename,separator):
    return pd.read_csv(
        path+filename, sep=separator, skip_blank_lines=True)

def toNumeric(df_saida):
    for k in list(df_saida):
        df_saida[k] = pd.to_numeric(df_saida[k], errors='ignore')
    return df_saida

def createDiasEstoqueDisponivel(df_saida):
    df_saida['dias_de_estoque_disponivel'] = df_saida.quantidade_em_estoque / df_saida.quantidade_vendida_media
    return df_saida.replace([np.inf, -np.inf], 'Sem vendas').fillna(0)

def toCSV(df_saida):
    df_saida.to_csv(r'./saida/relatorio.txt', index=None, sep=';')
    print('Arquivo relatorio.txt criado na pasta saida com sucesso!')