"""
Exercício 6: Fusão de Dicionários com Listas
Você tem dois dicionários representando o estoque de duas filiais de uma livraria:

filial_A = {"Python": 10, "JavaScript": 5, "Data Science": 8}

filial_B = {"Python": 4, "HTML": 12, "JavaScript": 2}

Crie um novo dicionário chamado estoque_total. Se o livro existir em ambas as 
filiais, some a quantidade; se existir em apenas uma, mantenha o valor.
"""

filial_A = {"Python": 10, "JavaScript": 5, "Data Science": 8}
filial_B = {"Python": 4, "HTML": 12, "JavaScript": 2}

estoque_total = filial_A.copy()

for livro in filial_B:
    if livro in estoque_total:
        estoque_total.update(
            {livro: estoque_total[livro] + filial_B[livro]}
        )
    else:
        estoque_total.update(
            {livro: filial_B[livro]}
        )

print(", ".join(f"{key}: {value}" for key, value in estoque_total.items()))