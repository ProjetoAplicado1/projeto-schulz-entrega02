from models.tecnico import Tecnico

def testar_tecnico():
    tecnico1 = Tecnico("101", "Ana", "Manhã")

    print("=== TESTE DA CLASSE TECNICO ===")
    print(f"Matrícula: {tecnico1.matricula}")
    print(f"Nome:      {tecnico1.nome}")
    print(f"Turno:     {tecnico1.turno}")
    print(f"Objeto:    {tecnico1}")

if __name__ == "__main__":
    testar_tecnico()