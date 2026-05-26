"""
Exercício 1: O Tradutor de Cores
Crie um dicionário chamado cores onde as chaves são nomes de cores em inglês 
e os valores são suas traduções em português (ex: "blue": "azul"). Peça para o 
usuário digitar uma cor em inglês e exiba a tradução. Se a cor não existir no 
dicionário, exiba uma mensagem de aviso.
"""

cores = {
    "blue":"azul", 
    "green":"verde", 
    "orange":"laranja", 
    "red":"vermelho"
}

escolha = input("Digite a cor em inglês: ")
if escolha in cores.keys():
    print(f"Tradução de {str(escolha).capitalize()}: {str(cores.get(escolha)).capitalize()}")
else:
    print("Cor não encontrada")