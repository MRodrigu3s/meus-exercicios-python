#https://github.com/MRodrigu3s/Sistema_CadAluno.git

alunos = []

while True:
    print()
    print("                                             BEM VINDO AO SISCAL")
    print("                                        SISTEMA DE CADASTRO DE ALUNOS")
    print()
    print("1 - Cadastrar Novo Aluno")
    print("2 - Listar Alunos Cadastrados")
    print("3 - Buscar Aluno por Matrícula")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do aluno: ")
        curso = input("Digite o curso do aluno: ")

        try:
            matricula = int(input("Digite a matrícula do aluno.\n(Coloque somente números): "))
        except ValueError:
            print("Matrícula inválida! Digite apenas números.")
            continue

        aluno = {
            "nome": nome,
            "matricula": matricula,
            "curso": curso
        }
        alunos.append(aluno)
        print("Aluno cadastrado com sucesso!")

    elif opcao == "2":
        if not alunos:
            print("Nenhum aluno cadastrado.")
        else:
            print("Lista de Alunos Cadastrados")
            for aluno in alunos:
                print(f"Nome: {aluno['nome']} | Matrícula: {aluno['matricula']} | Curso: {aluno['curso']}")

    elif opcao == "3":
        print('Consulte em "Lista de Alunos" o número de matrícula de um aluno')
        try:
            busca = int(input("Digite a matrícula do aluno que deseja buscar: "))
        except ValueError:
            print("Matrícula inválida! Digite apenas números.")
            continue

        encontrado = False
        for aluno in alunos:
            if aluno["matricula"] == busca:
                print(f"Aluno encontrado: Nome: {aluno['nome']} | Curso: {aluno['curso']}")
                encontrado = True
                break

        if not encontrado:
            print("Nenhum aluno encontrado com essa matrícula.")

    elif opcao == "4":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida! Tente novamente.")
