"""
Exercício 2: Lista de Compras com Tuplas
Crie uma lista chamada carrinho que armazene tuplas. 
Cada tupla deve conter o nome de um produto e o seu preço (ex: ("Maçã", 4.50)). 
Adicione pelo menos 4 produtos à lista, percorra-a com um laço e calcule o valor 
total da compra.
"""

lista = [
    ("Maçã", 4.50), 
    ("Banana", 6.50), 
    ("Abacate", 3.50), 
    ("Laranja", 6.50)
]


total = sum([preco for _, preco in lista])
print(total)