"""
Exercício 8: Inversão de Chave-Valor
Crie um dicionário com 5 itens (ex: {"A": 1, "B": 2, "C": 3}). 
Escreva um código que inverta esse dicionário, transformando os valores em 
chaves e as chaves em valores, gerando um novo dicionário 
(ex: {1: "A", 2: "B", 3: "C"}).
"""

original = {"A": 1, "B": 2, "C": 3}
invertido = {}

for key, value in original.items():
    invertido.update({value:key})
print(invertido)

resultado = {value:key for key, value in original.items()}
print(resultado)