# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 14:34:51 2023

@author: welly
"""

# Abrir o arquivo de notas em modo de escrita
with open('notas.txt', 'w') as arquivo:
    # Capturar o número de alunos
    num_alunos = int(input("Digite o número de alunos: "))
    
    # Loop pelos alunos e capturar suas notas
    for i in range(num_alunos):
        nome = input(f"Digite o nome do aluno {i+1}: ")
        nota1 = float(input(f"Digite a primeira nota do aluno {i+1}: "))
        nota2 = float(input(f"Digite a segunda nota do aluno {i+1}: "))
        nota3 = float(input(f"Digite a terceira nota do aluno {i+1}: "))
        
        # Escrever os dados no arquivo
        arquivo.write(f"{nome},{nota1},{nota2},{nota3}\n")

# Abrir o arquivo de notas em modo de leitura
with open('notas.txt', 'r') as arquivo:
    # Inicializar as listas de notas e nomes
    notas = []
    nomes = []
    
    # Loop pelas linhas do arquivo
    for linha in arquivo:
        # Separar os valores da linha pelo caractere ","
        valores = linha.split(",")
        nome = valores[0]
        nota1 = float(valores[1])
        nota2 = float(valores[2])
        nota3 = float(valores[3].strip())  # Remover o caractere de nova linha "\n"
        
        # Adicionar as notas e nomes às listas
        notas.append([nota1, nota2, nota3])
        nomes.append(nome)

# Calcular a média e o resultado dos alunos
for i in range(num_alunos):
    nome = nomes[i]
    nota1, nota2, nota3 = notas[i]
    media = (nota1 + nota2 + nota3) / 3
    
    if media >= 7:
        resultado = "Aprovado"
    elif media >= 4:
        resultado = "Exame"
    else:
        resultado = "Reprovado"
    
    # Exibir o resultado
    print(f"Aluno: {nome}\nMédia: {media:.1f}\nResultado: {resultado}\n")
