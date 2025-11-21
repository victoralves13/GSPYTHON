# FutureWork Network
integrantes:
Victor Oliveira Alves - 565723 
Joao Guilherme Guida - 565244

Analisador simples de perfis para o futuro do trabalho

O FutureWork Network é um pequeno sistema criado para organizar perfis de participantes e sugerir uma trilha profissional alinhada ao futuro do trabalho.
É um projeto direto, focado em raciocínio computacional e uso correto das estruturas pedidas na Global Solution.

# Objetivo do projeto

Criar uma aplicação básica em Python que:

receba perfis de usuários

aplique uma lógica simples de classificação

gere um relatório de recomendações

organize os dados em um DataFrame

ofereça opção de salvar tudo em CSV

Nada além disso. Simples, funcional e dentro dos requisitos.

# Estruturas exigidas pela GS e como foram utilizadas
 Entrada (input)

Feita na função coletar_perfis(), que solicita nome, área, experiência e disponibilidade.

# Saída (print / relatório)

A função relatorio() exibe as recomendações e a contagem por trilha.

# Repetição (loops)

Usado para processar cada perfil cadastrado e montar o DataFrame.

# Condição (if / elif / else)

Usado na classificação de área, validação da disponibilidade e na pontuação.

# Funções

O sistema está dividido em funções claras:
coletar_perfis, mostrar_perfis, classificar, montar_dataframe, relatorio, main.

Função dentro de função

Dentro de classificar() existe peso_exp(), que calcula o peso da experiência.

DataFrame (pandas)

Construído na função montar_dataframe(), organizado e ordenado por score.

Tudo foi usado com propósito, sem exagerar.

# Execute o programa:

python futurework_network.py


Cadastre quantos perfis quiser.

Escolha visualizar os perfis, gerar relatório e salvar CSV.

# Observações finais

O propósito do projeto não é prever carreiras reais, e sim demonstrar raciocínio computacional:
entrada, saída, repetição, condição, modularização, função interna e DataFrame.

O código é simples, direto e fácil de entender — exatamente como um protótipo deveria ser.
