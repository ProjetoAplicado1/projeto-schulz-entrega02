import sqlite3
from pathlib import Path

PASTA_PROJETO = Path(__file__).resolve().parent
CAMINHO_BANCO = PASTA_PROJETO / "banco.sqlite"

def conectar():
    conexao = sqlite3.connect(CAMINHO_BANCO)
    conexao.execute("PRAGMA foreign_keys = ON")
    return conexao