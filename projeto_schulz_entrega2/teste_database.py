
from database import conectar

conexao = conectar()
cursor = conexao.cursor()

for nome_tabela in ["tecnico", "equipamento", "medicao"]:
    print(f"\n=== TABELA: {nome_tabela} ===")

    cursor.execute(f"PRAGMA table_info({nome_tabela})")
    colunas = cursor.fetchall()

    for coluna in colunas:
        print(coluna[1])

conexao.close()
