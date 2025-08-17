
print()
print()
print("                                             CALCULADORA PARA CUSTO DE VIAGEM ")

print()

print('                                             TABELA DE VALORES DE COMBUSTIVÉIS ')

print()


print('                                         Etanol R$ 4,79')
print('                                         Gasolina Comum R$ 6,24')
print('                                         Gasolina Aditivada R$ 6,65')
print('                                         Diesel R$ 5,95')
print('                                         GNV R$ 4,59 (m³)')
print('                                         Carga Elétrica R$ 1,50 kWh (Vária de acordo com as estações públicas)')

print()

tipo_combustivel = str(input('Qual combustivel você costuma usar em seu carro? '))
print()
preco = float(input("Digite o preço da tabela que mostra o combustível que você irá usar: ").replace(",","."))
print()
distancia = float(input("Qual será a distância que você irá percorrer? ").replace('km','').replace('KM','').replace('kM','').replace('Km',''))
print()
combustivel = float(input('Quantos quilometros seu carro faz com um litro de combustivel? ').replace('km','').replace('KM','').replace('kM','').replace('Km',''))
print()
consumo_necessario = (distancia / combustivel)
print()
valor_total_gasto = (consumo_necessario * preco)

print()

print(f"Você irá usar {consumo_necessario:.2f} Litros de {tipo_combustivel} para chegar ao destino final")
print(f'Neste caso, você irá gastar R$ {valor_total_gasto:.2f} com combustivel'.replace('.',','))
print()

ajuda = str(input('Gostaria de algumas dicas para viajar em segurança? (sim ou Não) ').strip().lower())
if ajuda == "sim":
    print()
    print('- Revisão do veículo - verifique óleo, freios, pneus (inclusive o estepe), água do radiador, faróis e limpadores antes de sair.')
    print()
    print('- Documentos em dia - CNH, CRLV, seguro e, se necessário, documentação da viagem (como pedágios automáticos).')
    print() 
    print('- Planeje o trajeto - veja o melhor caminho no GPS, confira pontos de parada, pedágios e possíveis rotas alternativas.')
    print() 
    print('- Calibre os pneus - faça isso com o carro frio e ajuste de acordo com o peso da bagagem.')
    print() 
    print('- Leve um kit de emergência - chave de roda, triângulo, macaco, lanterna, carregador de celular, cabos de chupeta e primeiros socorros.')
    print() 
    print('- Respeite os limites de velocidade - além de evitar multas, garante mais segurança e economia de combustível.')
    print() 
    print('- Faça pausas a cada 2 horas - descansar ajuda a evitar sonolência e manter a atenção.')
    print() 
    print('- Hidrate-se e alimente-se bem - nada de dirigir com fome ou exagerar em comidas pesadas.')
    print() 
    print('- Divida a direção, se possível - se tiver outro motorista habilitado, reveze para evitar cansaço.')
    print() 
    print('- Entretenimento para a viagem - músicas, podcasts ou até joguinhos para os passageiros ajudam a tornar o trajeto mais agradável.')
    print()
    print('FAÇA UMA EXCELENTE VIAGEM') 
else:
    print('TUDO BEM! FAÇA UMA EXCELENTE VIAGEM')