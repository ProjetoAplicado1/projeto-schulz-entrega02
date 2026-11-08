from models.equipamento import Equipamento

def testar_equipamento():
    equipamento1 = Equipamento(
        tag_codigo="CAL-001",
        descricao="Paquimetro digital",
        setor_cliente="Metrologia"
    )

    print("=== TESTE DA CLASSE EQUIPAMENTO ===")
    print(f"Tag: {equipamento1.tag_codigo}")
    print(f"Descrição: {equipamento1.descricao}")
    print(f"Setor: {equipamento1.setor_cliente}")
    print(f"Representação do objeto: {equipamento1}")

if __name__ == "__main__":
    testar_equipamento()
    