"""
Exercício 3: Cadastro de Clientes
Desenvolva um programa que armazene o cadastro de 3 clientes. 
Cada cliente deve ser um dicionário com as chaves "nome", "idade" e "cidade". 
Todos esses dicionários devem ser guardados dentro de uma única lista chamada 
clientes. Ao final, exiba apenas o nome dos clientes que moram na cidade de 
"São Paulo".
"""

clientes = [
    {
        "nome": "Jonathas",
        "idade": 21,
        "cidade": "Iperó"
    },
    {
        "nome": "Davi",
        "idade": 46,
        "cidade": "Amazonas"
    },
    {        
        "nome": "Larissa",
        "idade": 39,
        "cidade": "São Paulo"
    }
]

nomes = [cliente.get("nome") for cliente in clientes]
print(", ".join([nome for nome in nomes]))