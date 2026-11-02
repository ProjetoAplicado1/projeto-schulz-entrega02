# SAECQ - Sistema de Automação e Emissão de Certificados de Qualidade
## Documentação Técnica do MVP - Parte 1 (Entrega 03)

**Empresa Parceira:** Schulz S.A.  
**Unidade Curricular:** Projeto Aplicado I - UniSENAI  
**Linguagem:** Python 3  
**Banco de Dados:** SQLite 3  

---

### 1. Padrões de Programação Orientada a Objetos (POO) Utilizados

A arquitetura do MVP foi concebida com foco em encapsulamento, coesão e separação clara de responsabilidades:

1. **Atributos e Encapsulamento:** As classes de domínio (`Tecnico`, `Equipamento` e `Medicao`) representam fielmente os elementos reais do laboratório de metrologia da Schulz S.A. Cada objeto guarda seus próprios atributos de estado.
2. **Regras de Negócio Metrológicas:** A validação de conformidade foi implementada na classe `Medicao`. Ela realiza o cálculo automático da média entre as leituras (`valor_obtidomean`), calcula o desvio (`erro_calculado`) e valida se a média está dentro do intervalo permitido $[valor\_nominal - tolerancia\_neg, valor\_nominal + tolerancia\_pos]$, atribuindo automaticamente `APROVADO` ou `REPROVADO`.
3. **Gerenciador de Persistência Decoplado:** A classe `BancoDeDados` no arquivo `database.py` é a única responsável pelas instruções SQL, garantindo o desacoplamento das regras de negócio em relação ao banco SQLite.

---

### 2. Diagrama Textual das Classes (UML)

```text
+------------------------------------+       +------------------------------------+
|              Tecnico               |       |            Equipamento             |
+------------------------------------+       +------------------------------------+
| - id_tecnico: int                  |       | - id_equipamento: int              |
| - matricula: str                   |       | - tag_codigo: str                  |
| - nome: str                        |       | - descricao: str                   |
| - turno: str                       |       | - setor_cliente: str               |
+------------------------------------+       +------------------------------------+
                  ^                                            ^
                  | (1)                                        | (1)
                  |                                            |
                  +---------------------+----------------------+
                                        | (N)
                      +------------------------------------+
                      |              Medicao               |
                      +------------------------------------+
                      | - id_medicao: int                  |
                      | - id_equipamento: int (FK)          |
                      | - id_tecnico: int (FK)             |
                      | - numero_certificado: str          |
                      | - data_calibracao: str             |
                      | - parametro_cota: str              |
                      | - valor_nominal: float             |
                      | - tolerancia_pos: float            |
                      | - tolerancia_neg: float            |
                      | - meas_1: float                    |
                      | - meas_2: float                    |
                      | - valor_obtidomean: float          |
                      | - erro_calculado: float            |
                      | - status_resultado: str            |
                      +------------------------------------+
                      | + calcular_media(): float          |
                      | + calcular_erro(): float           |
                      | + validar_tolerancia(): str        |
                      +------------------------------------+