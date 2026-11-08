# =========================================================
# UNIDADE CURRICULAR: PROJETO APLICADO I
# ARQUVIO INICIAL DE TESTE DO AMBIENTE
# =========================================================

#print("==================================================")
#print("  INICIANDO O PROJETO APLICADO I  ")
#print("==================================================")

#nome_aluno = input("Digite o seu nome completo:  ")
#projeto = input("Digite o nome de seu projeto:  ")

#print("---------------------------------")
#print(f"STATUS: Ambiente configurado com sucesso!")
#print(f"Aluno(a): {nome_aluno}")
#print(f"Projeto: {projeto}")
#print("Tudo pronto para iniciar o desenvolvimento!")
#print("--------------------------------------------------") 
#    *** FINAL DO SCRIPT TESTE ***


# =========================================================
# UNIDADE CURRICULAR: PROJETO APLICADO I
# SISTEMA DE METROLOGIA (SAECQ - SCHULZ S.A.)
# MAIN - EXECUÇÃO PRINCIPAL E DEMONSTRAÇÃO DO CRUD
# =========================================================

from database import (
    criar_tabelas, 
    inserir_medicao, 
    listar_medicoes_com_join, 
    atualizar_status_medicao, 
    deletar_medicao
)
from models.medicao import Medicao

def inicio():
    print("--------------------------------------------------")
    print("   SAECQ - SCHULZ S.A. | SISTEMA DE METROLOGIA    ")
    print("--------------------------------------------------")

    print("\n[1] Verificando e criando estrutura de tabelas...")    # Garante a criação das tabelas no SQLite
    criar_tabelas()

    print("\n[2] Cadastrando nova medição no sistema (CREATE)...")   # Instancia o Objeto de Domínio - Medicao (CREATE)
    med1 = Medicao(
        id_equipamento_fk=1,
        id_tecnico_fk=1,
        numero_certificado="CERT-2026-8801",
        data_calibracao="2026-10-24",
        parametro_cota="Diametro Interno A1",
        valor_nominal=50.00,
        tolerancia_pos=0.05,
        tolerancia_neg=0.05,
        meas_1=50.02,
        meas_2=50.03
    )

    med1.valor_obtidomean = med1.calcular_media()   # Execução dos cálculos da regra de negócio
    med1.erro_calculado = med1.calcular_erro()
    med1.status_resultado = med1.validar_tolerancia()

    id_gerado = inserir_medicao(med1)   # Salva no banco usando a função do database.py
    print(f"-> Medição salva com sucesso! ID gerado no banco: {id_gerado}")

    print("\n[3] Exibindo relatório de medições com JOIN (READ)...")    # Consulta com INNER JOIN (READ)
    medicoes = listar_medicoes_com_join()

    print("-----------------------------------------------------------------------------------------------------")
    print("ID | TAG EQUIP   | EQUIPAMENTO        | TÉCNICO        | COTA        | NOMINAL | MÉDIA | ERRO  | STATUS")
    print("-----------------------------------------------------------------------------------------------------")
    for item in medicoes:
        id_med = item[0]
        tag = item[1]
        equip = item[2]
        tecnico = item[3]
        cota = item[4]
        nom = item[5]
        media = item[6]
        erro = item[7]
        status = item[8]
        print(f"{id_med:<2} | {tag:<11} | {equip:<18} | {tecnico:<14} | {cota:<11} | {nom:<7.2f} | {media:<5.2f} | {erro:<5.2f} | {status}")
    print("-----------------------------------------------------------------------------------------------------")

    print("\n[4] Testando atualização de status (UPDATE)...")    # Atualização de Registro (UPDATE)
    atualizou = atualizar_status_medicao(id_gerado, "REPROVADO")
    if atualizou:
        print(f"-> Status do registro ID {id_gerado} alterado com sucesso para 'REPROVADO'.")

    print("\n[5] Testando remoção de registro (DELETE)...")    # Exclusão de Registro (DELETE)
    deletou = deletar_medicao(id_gerado)
    if deletou:
        print(f"-> Registro ID {id_gerado} removido com sucesso do banco de dados.")

    print("\n==========================================================")
    print("     DEMONSTRAÇÃO DE DADOS DO SISTEMA - RELATÓRIO CONCLUÍDO!           ")
    print("============================================================")

if __name__ == "__main__":
    inicio()



