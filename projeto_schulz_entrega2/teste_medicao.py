from models.medicao import Medicao

def testar_medicao():
    medicao1 = Medicao(
        id_equipamento_fk=1,
        id_tecnico_fk=1,
        numero_certificado="CERT-001",
        data_calibracao="2026-10-30",
        parametro_cota="Cota A",
        valor_nominal=10.0,
        tolerancia_pos=0.10,
        tolerancia_neg=0.10,
        meas_1=10.04,
        meas_2=10.06
    )

    print("=== TESTE DA CLASSE MEDICAO ===")
    print(f"Certificado: {medicao1.numero_certificado}")
    print(f"Data:        {medicao1.data_calibracao}")
    print(f"Parâmetro:   {medicao1.parametro_cota}")
    print(f"Média:       {medicao1.valor_obtidomean:.2f}")
    print(f"Erro:        {medicao1.erro_calculado:.2f}")
    print(f"Resultado:   {medicao1.status_resultado}")

if __name__ == "__main__":
    testar_medicao() 
    