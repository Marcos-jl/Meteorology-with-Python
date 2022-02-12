# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 19:32:40 2022

@author: Marcos
"""

#Importa a Classe principal
import index 

#input
capital = str(input('Qual capital deseja analisar ? ')) #Recebe a capital
analise = index.main(capital) #Cria um objeto e usa a capital como parâmetro
analise.extract(capital) #Executa o metódo de extração com a capital no parâmetro

#output
print('\t{} - Última Atualização\n'.format(analise.city))
print('{}'.format(analise.temp))
print('{}'.format(analise.data))
