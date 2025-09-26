#https://github.com/MRodrigu3s/meus-exercicios-python/tree/membro-uepa


class MembroUEPA:
    def __init__(self, nome, matricula, email):
        self.nome = nome
        self.matricula = matricula
        self.email = email

    def apresentar(self):
        print(f"Olá, sou um membro da UEPA. Nome: {self.nome}, Matrícula: {self.matricula}, Email: {self.email}")



class Aluno(MembroUEPA):
    def __init__(self, nome, matricula, email, curso):
        super().__init__(nome, matricula, email)
        self.curso = curso

    def verificar_notas(self):
        print(f"{self.nome} está verificando as notas no curso de {self.curso}.")

    def apresentar(self):
        print(f"Olá, sou o(a) aluno(a) {self.nome}, matriculado(a) em {self.curso}. Meu email é {self.email}.")



class Professor(MembroUEPA):
    def __init__(self, nome, matricula, email, departamento):
        super().__init__(nome, matricula, email)
        self.departamento = departamento

    def lancar_frequencia(self):
        print(f"{self.nome}, do departamento de {self.departamento}, está lançando a frequência.")

    def apresentar(self):
        print(f"Olá, sou o(a) professor(a) {self.nome}, do departamento de {self.departamento}. Contato: {self.email}.")



if __name__ == "__main__":
    print()
    print('AREA DO ALUNO:')
    aluno1 = Aluno("Ana Souza", "20251234", "ana.souza@uepa.br", "Programação")
    aluno1.apresentar()
    aluno1.verificar_notas()
    print()
    print('AREA DO PROFESSOR:')


    professor1 = Professor("Dr. Carlos Lima", "P00123", "carlos.lima@uepa.br", "Programação")
    professor1.apresentar()
    professor1.lancar_frequencia()
    print()
