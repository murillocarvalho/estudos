"""
Exercício 9: Agenda Telefônica Dinâmica
Crie um programa que simule uma agenda telefônica utilizando um dicionário. 
O usuário deve poder escolher entre três opções em um menu:

Inserir um novo contato (nome e telefone).

Buscar um telefone a partir do nome.

Sair do programa.
O programa deve rodar em um laço while até que a opção de sair seja escolhida.
"""
import inquirer

agenda_telefonica = {}
choices = [
    'Inserir um novo contato',
    'Buscar um telefone a partir do nome',
    'Mostrar agenda',
    'Sair do programa'
]
while True:
    questions = [
        inquirer.List(
            'opcao',
            message="Escolha uma opção",
            choices=choices),
    ]
    resposta = inquirer.prompt(questions)
    if choices.index(resposta['opcao']) == 0:
        nome = input("Digite o nome: ")
        telefone = input("Digite o telefone: ")
        agenda_telefonica[nome] = telefone
    if choices.index(resposta['opcao']) == 1:
        nome = input("Digite o nome: ")
        print(*[(chave, dado) for chave, dado in agenda_telefonica.items() if chave == nome])
    if choices.index(resposta['opcao']) == 2:
        print(*agenda_telefonica.items())
    if choices.index(resposta['opcao']) == 3:
        print("Até a próxima!")
        break
    print("\n")