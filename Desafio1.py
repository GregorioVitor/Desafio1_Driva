#Nome: Vitor Gregorio
#Desafio 1

import pandas as pd

#Ajuste para mostrar todas as linhas e colunas no terminal
#pd.set_option('display.max_rows', 1000)
#pd.set_option('display.max_columns', 9)

#Lendo o arquivo DadosEmpresa.csv e colocando ele em um dataFrame
arq = pd.read_csv('DadosEmpresa.csv')

#Mostrando o nome das colunas
print('Nome das Colunas:')
#print(arq.columns)
print(list(arq.columns)) #mostrando o nome das colunas de uma forma mais bonitinha
print()

#Mosrando as 5 primeiras linhas do arquivo
print('As cinco primeiras linhas: ')
print(arq.head())
print()

#Mostrando a quantidade de empresas que tem opcao_pelo_simples com valor SIM
opcao_sim = len(arq.query('opcao_pelo_simples == "SIM"'))
print('A quantidade de empresas com valor SIM é: '+ str(opcao_sim))
print()

#Mostrando a soma do capital_social de todas as empresas
soma_capital = arq['capital_social'].sum()
print('A soma do capital_social é: '+ str(soma_capital))
print()

#Mostrando todas as empresas que tem capital_social entre 10000 e 20000
print('As empresas que tem capital_social entre 10000 e 20000 são: ')
print(arq.query('capital_social > 10000 & capital_social <20000 '))
print()

#Lendo o arquivo DadosEndereco.csv e colocando ele em um dataFrame
print('Lendo segundo arquivo... ')
arq2 = pd.read_csv('DadosEndereco.csv')

#Realizando o merge entre os arquivos
print('Realizando o merge entre os arquivos... ')
Empresa_Endereco = pd.merge(arq, arq2, on='cnpj')

#Selecionando apenas as Empresas com o municipio com valor CURITIBA
print('Selecionando as empresas com municipio com valor CURITIBA... ')
Empresas_Curitiba = Empresa_Endereco.query('municipio =="CURITIBA"')

#Salvando o resultado no arquivo DadosCuritiba.csv
print('Salvando o resultado em DadosCuritiba.csv... ')
Empresas_Curitiba.to_csv('DadosCuritiba.csv')

print('Arquivo salvo!')
