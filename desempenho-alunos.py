print()
print("Alunos destaque")
print()
alunos = [
    {"matricula": "2025A01", "nome": "Ana Silva", "nota_final": 8.5, "frequencia": 80.0, "status_matricula": "ativo"},
    {"matricula": "2025A02", "nome": "Bruno Costa", "nota_final": 6.8, "frequencia": 95.0, "status_matricula": "ativo"},
    {"matricula": "2025A03", "nome": "Carla Dias", "nota_final": 4.5, "frequencia": 70.0, "status_matricula": "ativo"},
    {"matricula": "2025A04", "nome": "Daniel Farias", "nota_final": 9.5, "frequencia": 90.0, "status_matricula": "ativo"},
    {"matricula": "2025A05", "nome": "Elisa Mendes", "nota_final": 7.5, "frequencia": 65.0, "status_matricula": "desligado"},
    {"matricula": "2025A06", "nome": "Fábio Souza", "nota_final": 9.2, "frequencia": 75.0, "status_matricula": "ativo"},
    {"matricula": "2025A07", "nome": "Giovana Lima", "nota_final": 6.0, "frequencia": 100.0, "status_matricula": "ativo"},
    {"matricula": "2025A08", "nome": "Hugo Rocha", "nota_final": 7.0, "frequencia": 74.9, "status_matricula": "ativo"}
]

elegiveis = filter(lambda a: a["frequencia"] >= 75 and a["status_matricula"] == "ativo", alunos)

bonus = map(lambda a: {**a, "nota_final": min(a["nota_final"] * 1.1, 10)}, elegiveis)

destaques = filter(lambda a: a["nota_final"] >= 9, bonus)


for d in destaques:
    print(f"{d['nome']} | Nota Final: {d['nota_final']:.2f}")
