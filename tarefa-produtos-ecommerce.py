#https://github.com/MRodrigu3s/meus-exercicios-python/tree/tarefa-produtos-ecommerce.py

from abc import ABC, abstractmethod

class Produto(ABC):
    def __init__(self, nome: str, preco_base: float):
        self.nome = nome
        self.preco_base = preco_base

    @abstractmethod
    def calcular_preco_final(self) -> float:
        pass


class ProdutoFisico(Produto):
    def __init__(self, nome: str, preco_base: float, custo_frete: float):
        super().__init__(nome, preco_base)
        self.custo_frete = custo_frete

    def calcular_preco_final(self) -> float:
        return self.preco_base + self.custo_frete

class ProdutoDigital(Produto):
    def __init__(self, nome: str, preco_base: float, taxa_servico: float):
        super().__init__(nome, preco_base)
        self.taxa_servico = taxa_servico

    def calcular_preco_final(self) -> float:
        return self.preco_base + self.taxa_servico

def main():
    carrinho = [
        ProdutoFisico("Livro: Além do Horizonte", 50.0, 10.0),
        ProdutoDigital("E-book: Sucos para secar", 30.0, 5.0),
        ProdutoFisico("Caneca Harry Potter", 25.0, 8.0),
        ProdutoDigital("Curso Online: Máquina de Dinheiro", 100.0, 15.0)
    ]

    total = 0.0

    print("Resumo da Compra:")
    print("-" * 40)

    for produto in carrinho:
        preco_final = produto.calcular_preco_final()
        print(f"{produto.nome} - Preço Final: R$ {preco_final:.2f}")
        total += preco_final

    print("-" * 40)
    print(f"Total da Compra: R$ {total:.2f}")


if __name__ == "__main__":
    main()
