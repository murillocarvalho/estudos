"""
Exercício 10: Análise de Notas com Dicionário de Listas
Crie um dicionário onde as chaves são os nomes de 3 alunos e os valores são 
listas contendo 4 notas de cada um. O programa deve calcular a média de cada 
aluno e exibir o nome do aluno ao lado de sua média final.
"""

notas = {"Ana": [1,2,3,4], "Carol": [5,6,7,8], "Vitoria": [9,10,10,10]}

# medias = [(aluno, sum(nota)/4) for aluno, nota in notas.items()]

medias = {aluno: sum(nota)/4 for aluno, nota in notas.items()}

print(*medias.items(), sep="\n")

"""
CUIDADO: ao usar dict comprehension com {aluno, media for .....} cria um set invés de dicionario
"""