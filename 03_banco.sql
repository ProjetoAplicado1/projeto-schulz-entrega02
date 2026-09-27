/* CONSIDERAÇÕES:
O comando PRAGMA é um comando de configuração interno exclusivo do SQLite. 
Usamos o PRAGMA foreign_keys = ON; na primeira linha do nosso script para ligar a validação de Chaves Estrangeiras, 
garantindo que o banco de dados force a integridade referencial exigida pelas normas de qualidade da Schulz S.A.

A instrução ON DELETE RESTRICT foi usada para garantir que nenhum técnico ou equipamento com histórico de medição seja deletado, 
preservando a auditabilidade da ISO 9001. E a instrução ON UPDATE CASCADE foi usada pois, caso um ID seja atualizado no cadastro principal, 
o banco analise essa alteração automaticamente em todas as medições filhas sem deixar dados órfãos. */

-- PROJETO APLICADO I - UniSENAI
-- Empresa: Schulz S.A. | Laboratório de Metrologia
-- Script DDL de Criação do Banco SQLite


PRAGMA foreign_keys = ON;      -- Ativa o suporte e a validação estrita de Chaves Estrangeiras no SQLite
-- 1. TABELA: tecnico
-- Armazena o cadastro permanente dos metrologistas e operadores
CREATE TABLE IF NOT EXISTS tecnico (
    id_tecnico INTEGER PRIMARY KEY AUTOINCREMENT,
    matricula TEXT NOT NULL UNIQUE,
    nome TEXT NOT NULL,
    turno TEXT NOT NULL
);

-- 2. TABELA: equipamento
-- Armazena o cadastro dos ativos e instrumentos submetidos à calibração
CREATE TABLE IF NOT EXISTS equipamento (
    id_equipamento INTEGER PRIMARY KEY AUTOINCREMENT,
    tag_codigo TEXT NOT NULL UNIQUE,
    descricao TEXT NOT NULL,
    setor_cliente TEXT NOT NULL
);

-- 3. TABELA: medicao
-- Tabela transacional que regista as medições da MMC Zeiss
CREATE TABLE IF NOT EXISTS medicao (
    id_medicao INTEGER PRIMARY KEY AUTOINCREMENT,
    id_equipamento_fk INTEGER NOT NULL,
    id_tecnico_fk INTEGER NOT NULL,
    numero_certificado TEXT NOT NULL UNIQUE,
    data_calibracao TEXT NOT NULL,
    parametro_cota TEXT NOT NULL,
    valor_nominal REAL NOT NULL,
    tolerancia_pos REAL NOT NULL,
    tolerancia_neg REAL NOT NULL,
    meas_1 REAL NOT NULL,
    meas_2 REAL NOT NULL,
    valor_obtidomean REAL NOT NULL,
    erro_calculado REAL NOT NULL,
    status_resultado TEXT NOT NULL CHECK (status_resultado IN ('APROVADO', 'REPROVADO')),
    
    -- Definição das Chaves Estrangeiras (Integridade Referencial)
    FOREIGN KEY (id_equipamento_fk) REFERENCES equipamento (id_equipamento) 
        ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (id_tecnico_fk) REFERENCES tecnico (id_tecnico) 
        ON DELETE RESTRICT ON UPDATE CASCADE
);

