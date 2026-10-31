
from models.equipamentos import Equipamento

equipamento1 = Equipamento(
    "CAL-001",
    "Paquimetro digital",
    "Metrologia"
)

print("=== TESTE DA CLASSE EQUIPAMENTO ===")
print(f"Tag: {equipamento1.tag_codigo}")
print(f"Descrição: {equipamento1.descricao}")
print(f"Setor: {equipamento1.setor_cliente}")
