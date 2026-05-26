"""
Exercício 7: Mineração de Dados em Tuplas
Dada uma tupla contendo vários números inteiros: numeros = 
(12, 45, 78, 2, 19, 45, 8, 12, 99, 45)
Escreva um programa que encontre e exiba:

O maior número da tupla.

O menor número da tupla.

Quantas vezes o número 45 se repete.
"""

numeros = (12, 45, 78, 2, 19, 45, 8, 12, 99, 45)

print(f"Maior: {max(numeros)}\nMenor: {min(numeros)}\nRepetições de 45: {numeros.count(45)}")