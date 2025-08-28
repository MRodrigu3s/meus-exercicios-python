
# https://github.com/MRodrigu3s/tarefa-inventario.git

carrinho_compras = []

print('                                                      BEM VINDO AO ELETRO.py')
print('')
print('Por favor, adicione itens ao carrinho selecionando "adicionar"')
print('Caso queira remover algum item do carrinho, selecione "remover"')
print('E se desejar ver seus itens do carrinho, selecione "visualizar lista"')
print('E se desejar encerrar as compras, selecione "finalizar"')
print()
print('')

while True:
    comando = input('O que você deseja? ').lower()

    if comando == 'adicionar':
        nome_produto = input('Qual produto você quer adicionar? ')
        quantidade = int(input(f"Qual a quantidade de {nome_produto}? "))

        lista_produtos = {
            "Nome": nome_produto,
            "Quantidade": quantidade,
        }

        carrinho_compras.append(lista_produtos)
        print('')
        print(f"{quantidade} unidade(s) de {nome_produto} adicionada(s) ao carrinho!")

    elif comando == 'visualizar lista':
        if len(carrinho_compras) == 0:
            print("Sua lista não possui itens. Volte às compras agora!")
        else:
            print(f"Você tem {len(carrinho_compras)} produto(s):")
            for i, item in enumerate(carrinho_compras, start=1):
                print(f"{i}. {item['Nome']} - Quantidade: {item['Quantidade']}")

    elif comando == 'remover':
        if len(carrinho_compras) == 0:
            print("Não há nada para remover.")
        else:
            for i, item in enumerate(carrinho_compras, start=1):
                print(f"{i}. {item['Nome']} - Quantidade: {item['Quantidade']}")
            lista_remover = int(input("Digite o número do produto para remover: "))
            if 1 <= lista_remover <= len(carrinho_compras):
                removido = carrinho_compras.pop(lista_remover - 1)
                print(f"{removido['Nome']} removido do carrinho.")
            else:
                print("Número inválido.")

    elif comando == 'finalizar':
        print("Compra finalizada. Seu carrinho contém:")
        print('')
        for item in carrinho_compras:
            print(f"- {item['Nome']} - Quantidade: {item['Quantidade']}")
        print('')
        print("Total de itens:", sum(item["Quantidade"] for item in carrinho_compras))
        print('')

        break

    else:
        print('')
        print("Comando não reconhecido. Tente novamente.")
        print('')
        
