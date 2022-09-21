from primeiro.lib.interface import *

alunos = [[123, "rene", 32, {"por": 9, "calc": 3, "alp": 5}], [321, "jose", 60, dict()]]


cabecalho("BEM-VINDO AO SITEMA DE GESTÃO ACADÊMICO")

cabecalho("MENU PRINCIPAL")

opcao = 99

while opcao != 0:
    print("1-Cadrastar alunos ")
    print("2-Listar alunos ")
    print("3-Buscar alunos por CPF ")
    print("4-Buscar aluno pelo o nome ")
    print("5-Atualizar idade do aluno aluno pelo o CPF ")
    print("6-Inserir nota da Disciplina ")
    print("7-Mostrar gráficos de notas ")
    print("8-Mostrar CRE do aluno")
    print("0-Sair")
    opcao = int(input("\nDigite a opção: "))

    if opcao == 1:
        cadastrar(alunos)
        print("Aluno cadastrado com sucesso!")
    elif opcao == 2:
        listar(alunos)
    elif opcao == 3:
        print(buscarcpf(alunos))
    elif opcao == 4:
        print(buscarnome(alunos))
    elif opcao == 5:
        print(atualizaridade(alunos))
    elif opcao == 6:
        print(inserirnotas(alunos))
    elif opcao == 7:
        print(plotnotas(alunos))
    elif opcao == 8:
        print(calcular_cre(alunos))
    else:
        print("Opção invalida")
        cabecalho("Digite uma opcão valida")


print("\nAté logo")

exit()