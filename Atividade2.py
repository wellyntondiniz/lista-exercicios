# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 21:02:10 2023

@author: welly
"""

with open("notas.txt", "r") as arquivo:
    texto = arquivo.read();
    lista = texto.split(",")
    
    media = (float(lista[1]) + float(lista[2]) + float(lista[3])) /3;
    resultado = "";
    if (media >= 7):
        resultado = "aprovado.txt"
    elif (media >= 5):
        resultado = "exame.txt"
    else:
        resultado = "reprovado.txt"
    
    with open(resultado, "w") as resultado:
        legenda = lista[0] + "," + str(media)
        resultado.write(legenda)
    
    
    