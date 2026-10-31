
from models.tecnico import Tecnico

tecnico1 = Tecnico("101", "Ana", "Manhã")

print("=== TESTE DA CLASSE TECNICO ===")
print(f"Matrícula: {tecnico1.matricula}")
print(f"Nome: {tecnico1.nome}")
print(f"Turno: {tecnico1.turno}")
