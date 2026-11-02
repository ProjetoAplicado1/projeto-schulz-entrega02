# Projeto Aplicado - Sistema Metrológico (Schulz)

Este repositório contém o início do desenvolvimento de um sistema de gestão metrológica e validação de medições de equipamentos, visando atender as demandas da empresa parceira da UNISENAI - Schulz S.A

---

## 🚀 Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Banco de Dados:** SQLite 3
* **Controlo de Versão:** Git & GitHub

---

## 📁 Estrutura do Projeto

```text
Projeto_Aplicado_1/
├── projeto_schulz_entrega2/
│   ├── models/
│   │   ├── equipamento.py   # Classe de domínio Equipamento
│   │   ├── medicao.py       # Regras de negócio e tolerância metrológica
│   │   └── tecnico.py       # Classe de domínio Técnico
│   ├── 01_estrutura.md      # Documentação da arquitetura inicial
│   ├── 02_dicionario.md     # Dicionário de dados
│   ├── 03_banco.sql         # Script SQL de criação das tabelas
│   ├── 06_mvp_parte1.md     # Especificação funcional do MVP
│   ├── banco.sqlite         # Ficheiro do banco de dados local
│   ├── database.py          # Módulo de conexão e persistência
│   └── main.py              # Ponto de entrada do sistema
├── .gitignore               # Configuração de ficheiros ignorados pelo Git
└── README.md                # Documentação principal


🛠️ Como Executar o Projeto
1. Clonar o repositório: (Bash)

git clone [https://github.com/ProjetoAplicado1/projeto-schulz-entrega02.git](https://github.com/ProjetoAplicado1/projeto-schulz-entrega02.git)
cd projeto-schulz-entrega02

2. Executar a aplicação: (Bash)

python projeto_schulz_entrega2/main.py

📌 Histórico de Versões 
v1.0.1
v1.0.0
v0.3.0
v0.2.0
v0.1.0

👥 Equipe: Grupo 12
André Rodrigo Miranda, 
Fabiana de Oliveira Gomes, 
Jonathan Stülp Zoz, 
Tatiana Marques Domingos

