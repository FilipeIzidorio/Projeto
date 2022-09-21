import matplotlib.pyplot as plt


def linha(tam=45):
    return "-" * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(45))
    print(linha())


def cadastrar(lista: list):
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    cpf = int(input("Digite o numeros do seu CPF: "))
    lista.append([cpf, nome, idade, dict()])


def listar(lista: list):
    if len(lista) > 0:
        for aluno in lista:
            print(f"\nnome:{aluno[1]}")
            print(f"CPF:{aluno[0]}")
            print(f'idade:{aluno[2]}')
            print("\n")
    else:
        cabecalho("Não existe nenhum aluno cadastrado")


def buscarcpf(lista: list):
    cpf = int(input("\nDigite o CPF do aluno: "))
    achei = False
    aluno_encontrado = []
    for aluno in lista:
        if cpf == aluno[0]:
            achei = True
            print(f"\nnome:{aluno[1]}")
            print(f"CPF:{aluno[0]}")
            print(f'idade:{aluno[2]}')
            aluno_encontrado = aluno
            break
    if not achei:
        cabecalho("Usuário não encotrado")
    return [achei, cpf, aluno_encontrado]


def buscarnome(lista: list):
    nome = input("Digite o nome do aluno")
    for aluno in lista:
        if nome in aluno[1]:
            print("___________________")
            print(f"\nnome:{aluno[1]}")
            print(f"CPF:{aluno[0]}")
            print(f'idade:{aluno[2]}')


def atualizaridade(lista: list):
    respostas = buscarcpf(lista)
    if respostas:
        nova_idade = int(input("Digite a nova idade"))
        cpf = respostas[1]
        for i in range(len(lista)):
            if cpf == lista[1][0]:
                lista[1][0] = nova_idade
                break


def inserirnotas(lista_alunos: list):
    buscarnome(lista_alunos)
    cpf = int(input("Digite o CPF do aluno:"))
    for i in range(len(lista_alunos)):
        if cpf == lista_alunos[i][0]:
            nome_disciplina = input("Digite o nome da disciplina: ")
            nota = float(input("Digite sua nota: "))
            lista_alunos[i][3][nome_disciplina] = nota


def plotnotas(lista: list):
    rertono = buscarcpf(lista)
    if rertono[0]:
        aluno = rertono[2]

        plt.figure(figsize=(9, 5))
        coluna = aluno[3].keys()
        linhas = aluno[3].values()
        plt.bar(coluna, linhas)
        plt.suptitle("Notas do aluno")
        plt.show()


def calcular_cre(lista: list):
    rertono = buscarcpf(lista)
    if rertono[0]:
        aluno = rertono[2]
        nota = list(aluno[3].values())
        media = sum(nota) / len(nota)
        print(f"\n CRE do aluno: {round(media,2)}")
