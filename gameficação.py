from abc import ABC, abstractmethod
import random
import time


class Personagem(ABC):
    def __init__(self, nome, vida, autoataque):
        self.nome = nome
        self._vida = vida
        self._autoataque = autoataque

    def receber_dano(self, dano):
        dano_real = max(0, dano)
        self._vida = max(0, self._vida - dano_real)
        print(f"{self.nome} recebeu {dano_real} de dano. Vida atual: {self._vida}")

    def esta_vivo(self):
        return self._vida > 0

    @abstractmethod
    def atacar(self, alvo):
        pass



class Guerreiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome, vida=150, autoataque=20)
        self.__furia = 50

    def atacar(self, alvo):
        print(f"{self.nome} ataca com espada!")
        dano = self._autoataque
        self.__aumentar_furia(10)
        alvo.receber_dano(dano)

    def ataque_especial(self, alvo):
        custo_furia = 30
        if self.__furia >= custo_furia:
            dano = self._autoataque + 30
            self.__furia -= custo_furia
            print(f"{self.nome} usa ATAQUE ESPECIAL! (Fúria restante: {self.__furia})")
            alvo.receber_dano(dano)
        else:
            print(f"{self.nome} tentou usar ataque especial, mas não tem fúria suficiente ({self.__furia}).")
            self.atacar(alvo)

    def __aumentar_furia(self, valor):
        self.__furia = min(100, self.__furia + valor)

    def get_furia(self):
        return self.__furia


class Mago(Personagem):
    def __init__(self, nome):
        super().__init__(nome, vida=100, autoataque=15)
        self.__mana = 100

    def atacar(self, alvo):
        custo_mana = 20
        if self.__mana >= custo_mana:
            dano = self._autoataque + 10
            self.__mana -= custo_mana
            print(f"{self.nome} lança uma bola de fogo! (Mana restante: {self.__mana})")
            alvo.receber_dano(dano)
        else:
            print(f"{self.nome} está sem mana suficiente ({self.__mana}), ataca com cajado!")
            dano = self._autoataque // 2
            alvo.receber_dano(dano)

    def regenerar_mana(self, valor):
        self.__mana = min(100, self.__mana + valor)

    def get_mana(self):
        return self.__mana


def batalha():
    guerreiro = Guerreiro("Master Yi")
    mago = Mago("Veigar")

    turno = 1
    while guerreiro.esta_vivo() and mago.esta_vivo():
        print(f"\n--- Turno {turno} ---")

        if random.random() < 0.4:
            guerreiro.ataque_especial(mago)
        else:
            guerreiro.atacar(mago)


        if not mago.esta_vivo():
            print(f"{mago.nome} foi derrotado!")
            break


        mago.atacar(guerreiro)
        mago.regenerar_mana(10)


        if not guerreiro.esta_vivo():
            print(f"{guerreiro.nome} foi derrotado!")
            break

        turno += 1
        time.sleep(1)

    print("\n--- Fim da batalha ---")
    if guerreiro.esta_vivo():
        print(f"{guerreiro.nome} venceu!")
    else:
        print(f"{mago.nome} venceu!")


if __name__ == "__main__":
    batalha()
