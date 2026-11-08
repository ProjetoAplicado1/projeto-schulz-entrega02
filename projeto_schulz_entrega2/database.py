import sqlite3
from pathlib import Path

PASTA_PROJETO = Path(__file__).resolve().parent
CAMINHO_BANCO = PASTA_PROJETO / "banco.sqlite"

def conectar():
    conexao = sqlite3.connect(CAMINHO_BANCO)
    conexao.execute("PRAGMA foreign_keys = ON")
    return conexao

def criar_tabelas():
    """Cria a estrutura das tabelas no SQLite caso não existam."""
    conexao = conectar()
    cursor = conexao.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tecnico (
        id_tecnico INTEGER PRIMARY KEY AUTOINCREMENT,
        matricula TEXT NOT NULL UNIQUE,
        nome TEXT NOT NULL,
        turno TEXT
    );
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS equipamento (
        id_equipamento INTEGER PRIMARY KEY AUTOINCREMENT,
        tag_codigo TEXT NOT NULL UNIQUE,
        descricao TEXT NOT NULL,
        setor_cliente TEXT
    );
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS medicao (
        id_medicao INTEGER PRIMARY KEY AUTOINCREMENT,
        id_equipamento_fk INTEGER NOT NULL,
        id_tecnico_fk INTEGER NOT NULL,
        numero_certificado TEXT,
        data_calibracao TEXT,
        parametro_cota TEXT,
        valor_nominal REAL,
        tolerancia_pos REAL,
        tolerancia_neg REAL,
        meas_1 REAL,
        meas_2 REAL,
        valor_obtidomean REAL,
        erro_calculado REAL,
        status_resultado TEXT,
        FOREIGN KEY (id_equipamento_fk) REFERENCES equipamento (id_equipamento),
        FOREIGN KEY (id_tecnico_fk) REFERENCES tecnico (id_tecnico)
    );
    """)
    
    conexao.commit()
    conexao.close()


def inserir_medicao(medicao):     # 1. CREATE (INSERIR)
    """Insere um novo registro de medição no banco de dados."""
    conexao = conectar()
    cursor = conexao.cursor()
    
    query = """
    INSERT INTO medicao (
        id_equipamento_fk, id_tecnico_fk, numero_certificado, data_calibracao,
        parametro_cota, valor_nominal, tolerancia_pos, tolerancia_neg,
        meas_1, meas_2, valor_obtidomean, erro_calculado, status_resultado
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    
    valores = (
        medicao.id_equipamento_fk, medicao.id_tecnico_fk, medicao.numero_certificado,
        medicao.data_calibracao, medicao.parametro_cota, medicao.valor_nominal,
        medicao.tolerancia_pos, medicao.tolerancia_neg, medicao.meas_1,
        medicao.meas_2, medicao.valor_obtidomean, medicao.erro_calculado,
        medicao.status_resultado
    )
    
    cursor.execute(query, valores)
    conexao.commit()
    id_gerado = cursor.lastrowid
    conexao.close()
    return id_gerado


def listar_medicoes_com_join():    # 2. READ (CONSULTAR / BUSCAR COM JOIN)
    """Realiza uma consulta relacional utilizando INNER JOIN entre as 3 tabelas."""
    conexao = conectar()
    cursor = conexao.cursor()
    
    query = """
    SELECT 
        m.id_medicao,
        e.tag_codigo,
        e.descricao AS equipamento,
        t.nome AS tecnico,
        m.parametro_cota,
        m.valor_nominal,
        m.valor_obtidomean,
        m.erro_calculado,
        m.status_resultado
    FROM medicao m
    INNER JOIN equipamento e ON m.id_equipamento_fk = e.id_equipamento
    INNER JOIN tecnico t ON m.id_tecnico_fk = t.id_tecnico;
    """
    
    cursor.execute(query)
    resultados = cursor.fetchall()
    conexao.close()
    return resultados


def atualizar_status_medicao(id_medicao, novo_status):     # 3. UPDATE (ATUALIZAR)
    """Atualiza o status de um registro de medição existente."""
    conexao = conectar()
    cursor = conexao.cursor()
    
    query = "UPDATE medicao SET status_resultado = ? WHERE id_medicao = ?"
    cursor.execute(query, (novo_status, id_medicao))
    
    conexao.commit()
    linhas_alteradas = cursor.rowcount
    conexao.close()
    return linhas_alteradas > 0


def deletar_medicao(id_medicao):      # 4. DELETE (DELETAR)
    """Remove uma medição do banco de dados pelo ID."""
    conexao = conectar()
    cursor = conexao.cursor()
    
    query = "DELETE FROM medicao WHERE id_medicao = ?"
    cursor.execute(query, (id_medicao,))
    
    conexao.commit()
    linhas_alteradas = cursor.rowcount
    conexao.close()
    return linhas_alteradas > 0