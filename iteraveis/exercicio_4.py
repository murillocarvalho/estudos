"""
Exercício 4: Filtrando Tuplas em Listas
Dada a seguinte lista de tuplas representando alunos e suas respectivas notas:
alunos = [("Ana", 8.5), ("Pedro", 6.0), ("Maria", 9.2), ("João", 5.5)]
Crie uma nova lista chamada aprovados e adicione a ela apenas o nome dos alunos 
que obtiveram nota maior ou igual a 7.0.
"""

alunos = [("Ana", 8.5), ("Pedro", 6.0), ("Maria", 9.2), ("João", 5.5)]

aprovados = []
for aluno in alunos:
    if aluno[1] >= 7:
        aprovados.append(aluno[0])

print("Alunos aprovados: ", ", ".join(aprovados))