# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 20:41:15 2023

@author: wellynton
"""
with open("notas.txt", "w") as arquivo:
    nome = input("Nome")
    nota1 = input("Nota 1")
    nota2 = input("Nota 2")
    nota3 = input("Nota 3")
    linha = nome + "," + nota1 + "," + nota2 + "," + nota3;
    arquivo.write(linha);
