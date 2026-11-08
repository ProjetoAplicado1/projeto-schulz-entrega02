from models.tecnico import Tecnico
from models.equipamento import Equipamento  
from models.medicao import Medicao

def testar_classes():
    print("=== TESTE DE IMPORTAÇÃO E INSTANCIAÇÃO DAS CLASSES ===")
    
    tec = Tecnico("M-3042", "Técnico Um", "1º Turno")    # Instancia simulada para validar métodos
    eq = Equipamento("MMC-ZEISS-01", "Máquina Tridimensional", "Usinagem")
    med = Medicao(1, 1, "CERT-001", "2026-11-08", "Cota A", 10.0, 0.1, 0.1, 10.02, 10.04)

    print(f"✅ Classe Tecnico: {tec}")
    print(f"✅ Classe Equipamento: {eq}")
    print(f"✅ Classe Medicao: {med}")

    print("\nTodas as classes foram importadas e instanciadas com sucesso!")

if __name__ == "__main__":
    testar_classes()