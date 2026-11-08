import sqlite3
from database import (
    conectar,
    criar_tabelas, 
    inserir_medicao, 
    listar_medicoes_com_join, 
    atualizar_status_medicao, 
    deletar_medicao
)
from models.medicao import Medicao

def garantir_dados_base():
    """Insere registros base de técnico e equipamento se a base estiver vazia."""
    conexao = conectar()
    cursor = conexao.cursor()
    
    # Inserção para permitir testes no banco
    cursor.execute("INSERT OR IGNORE INTO tecnico (id_tecnico, matricula, nome, turno) VALUES (1, 'M-TESTE', 'Técnico Teste', '1º Turno');")
    cursor.execute("INSERT OR IGNORE INTO equipamento (id_equipamento, tag_codigo, descricao, setor_cliente) VALUES (1, 'TAG-TESTE', 'Equipamento Teste', 'Laboratório');")
    
    conexao.commit()
    conexao.close()

def testar_operacoes_banco():
    print("=== 1. CRIANDO E ESTRUTURANDO TABELAS ===")
    criar_tabelas()
    garantir_dados_base()
    print("Tabelas e registros de teste verificados com sucesso!")

    print("\n=== 2. TESTANDO INSERÇÃO (CREATE) ===")
    nova_medicao = Medicao(
        id_equipamento_fk=1,
        id_tecnico_fk=1,
        numero_certificado="CERT-2026-001",
        data_calibracao="2026-03-30",
        parametro_cota="Comprimento",
        valor_nominal=10.0,
        tolerancia_pos=0.1,
        tolerancia_neg=0.1,
        meas_1=10.04,
        meas_2=10.06
    )

    id_gerado = inserir_medicao(nova_medicao)
    print(f"Medição cadastrada com sucesso! ID gerado no banco: {id_gerado}")

    print("\n=== 3. TESTANDO CONSULTA COM JOIN (READ) ===")
    medicoes = listar_medicoes_com_join()
    for item in medicoes:
        print(f"ID: {item[0]} | Tag: {item[1]} | Equipamento: {item[2]} | Técnico: {item[3]} | Status: {item[8]}")

    print("\n=== 4. TESTANDO ATUALIZAÇÃO (UPDATE) ===")
    sucesso_update = atualizar_status_medicao(id_gerado, "REPROVADO")
    if sucesso_update:
        print(f"Status do registro ID {id_gerado} atualizado com sucesso!")

    print("\n=== 5. TESTANDO EXCLUSÃO (DELETE) ===")
    sucesso_delete = deletar_medicao(id_gerado)
    if sucesso_delete:
        print(f"Registro ID {id_gerado} removido do banco com sucesso!")

if __name__ == "__main__":
    testar_operacoes_banco()