# ETL
### Regras de negócio definidas
Estoque: Se o valor de estoque vir duplicado, é considerado  o último valor inserido;

Cadastro: Nos casos de Ids duplicadas foram considero o primeiro inserido e removidos os demais;

Vendas: Caso o valor de vendas venha duplicado, são removidos, entretando se o id for igual mas o valor diferente, ambos são considerados fazendo a soma;

Saida: A coluna de dias disponíveis foi feita usando a média de vendas

### Testes
Na pasta testes_files estão arquivos no formato que serão inseridos na pasta de entrada. Eles são usados nos testes unitários. Dentro do arquivo de teste há dataframes que serão usados para comparar se as funções executaram de maneira correta.

Os testes são executados antes da main principal, caso tenha mudança em uma função da service os testes mostrarão se o código irá quebrar.


### Requisitos e Instalação 
#### Requisitos:
```python
Python 3.8
Numpy 1.19.4
Pandas 1.1.5
```
#### Instalação
Idle recomendada Pycharm.

Executar o arquivo 
```python
__main__.py 
```

