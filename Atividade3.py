# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 21:33:25 2023

@author: welly
"""

with open("exame.txt") as arquivo:
    texto = arquivo.read();
    lista = texto.split(",")
    nota_exame = float(input("Nota exame: "))
    
    media = float(lista[1])
    
    media_final = (nota_exame + media) /2
    
    if (media >= 5):
        resultado = "aprovado.txt"
    else:
        resultado = "reprovado.txt"
    
    with open(resultado, "w") as resultado:
        legenda = lista[0] + "," + str(media_final) + " por exame"
        resultado.write(legenda)