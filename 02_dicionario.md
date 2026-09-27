<!--Dicionário de Dados - CONSIDERAÇÕES
* Objetivo:
=> O Diagrama (ERD) mostra a 'foto' geral das tabelas, mas o Dicionário de Dados é o manual de especificações técnicas do banco. Ele permite que qualquer programador ou auditor da ISO 9001/IATF 16949 entenda exatamente o tipo, o limite e a regra de cada informação guardada.

* Tipificação do Dados:
=> INTEGER (Inteiros): Usados para as chaves (id_tecnico, id_equipamento, id_medicao) para garantir buscas rápidas e incremento automático sequencial.   
=> TEXT (Textos): Usados para cadastros e códigos alfanuméricos como a matricula, tag_codigo, numero_certificado e status_resultado.   
=> REAL (Números Decimais/Flutuantes): Usados exclusivamente para as variáveis e medições metrológicas (valor_nominal, meas_1, valor_obtidomean, erro_calculado), pois exigem precisão de casas decimais em milímetros (mm) vindas da CMM Zeiss.   

* Uso do NOT NULL:
No contexto metrológico da Schulz S.A., não são aceitas medições 'pela metade' ou sem autor/responsável. Garantir que toda informação seja obrigatória (NOT NULL) evita laudos incompletos e garante rastreabilidade auditável total.

* No SQLite não existe o tipo nativo DATE e ENUM.
A recomendação da documentação do SQLite é utilizar TEXT com o padrão (YYYY-MM-DD). Isso garante que as funções temporais do banco funcionem perfeitamente e mantém a ordenação cronológica correta para os relatórios da Schulz S.A.. Para garantir que nenhum status inválido seja digitado no sistema do laboratório, usamos o tipo TEXT com uma restrição CHECK, simulando o comportamento exato de um ENUM e garantindo a integridade dos dados para a ISO 9001. -->


# 2. Dicionário de Dados do Sistema

Este documento apresenta o Dicionário de Dados do banco de dados relacional criado para o laboratório de metrologia da **Schulz S.A.** O objetivo é detalhar a estrutura de cada campo, seus tipos de dados no SQLite, restrições e regras de negócio associadas, atendendo aos padrões de auditoria ISO 9001 e IATF 16949.


## 2.1. Tabela: `tecnico`
Armazena os dados cadastrais dos operadores e metrologistas responsáveis pela execução dos ensaios.

| Nome do Campo | Tipo de Dado | Restrições | Descrição / Regra de Negócio |
| :--- | :--- | :--- | :--- |
| `id_tecnico` | `INTEGER` | `PRIMARY KEY AUTOINCREMENT` | Chave primária identificadora única do técnico no sistema. |
| `matricula` | `TEXT` | `UNIQUE`, `NOT NULL` | Número/código da matrícula do funcionário na Schulz S.A. |
| `nome` | `TEXT` | `NOT NULL` | Nome completo do operador/metrologista. |
| `turno` | `TEXT` | `NOT NULL` | Turno de trabalho do colaborador (ex: 1º Turno, 2º Turno, 3º Turno, ou Matutino e Noturno). |



## 2.2. Tabela: `equipamento`
Armazena os atributos cadastrais dos instrumentos e ativos submetidos à medição e calibração.

| Nome do Campo | Tipo de Dado | Restrições | Descrição / Regra de Negócio |
| :--- | :--- | :--- | :--- |
| `id_equipamento` | `INTEGER` | `PRIMARY KEY AUTOINCREMENT` | Chave primária identificadora única do equipamento. |
| `tag_codigo` | `TEXT` | `UNIQUE`, `NOT NULL` | Código de patrimônio/TAG de identificação do ativo (ex: TAG-703.1208). |
| `descricao` | `TEXT` | `NOT NULL` | Nome e especificações técnicas do equipamento ou dispositivo. |
| `setor_cliente` | `TEXT` | `NOT NULL` | Setor solicitante da calibração (ex: Usinagem I, Compressores). |



## 2.3. Tabela: `medicao`
Tabela transacional que contém os registros das medições dimensionais extraídas da MMC e os cálculos metrológicos resultantes.

| Nome do Campo | Tipo de Dado | Restrições | Descrição / Regra de Negócio |
| :--- | :--- | :--- | :--- |
| `id_medicao` | `INTEGER` | `PRIMARY KEY AUTOINCREMENT` | Chave primária identificadora única do registro de medição. |
| `id_equipamento_fk` | `INTEGER` | `FOREIGN KEY`, `NOT NULL` | Chave estrangeira vinculando a medição ao seu respectivo equipamento. |
| `id_tecnico_fk` | `INTEGER` | `FOREIGN KEY`, `NOT NULL` | Chave estrangeira vinculando a medição ao técnico executor. |
| `numero_certificado` | `TEXT` | `UNIQUE` `NOT NULL` | Código único do certificado de calibração gerado pelo laboratório. |
| `data_calibracao` | `TEXT` | `NOT NULL` | Data e hora de realização do ensaio no formato ISO (`YYYY-MM-DD`). |
| `parametro_cota` | `TEXT` | `NOT NULL` | Descrição do elemento geométrico inspecionado (ex: Diâmetro A, Comprimento B). |
| `valor_nominal` | `REAL` | `NOT NULL` | Dimensão nominal do desenho técnico de engenharia (em mm). |
| `tolerancia_pos` | `REAL` | `NOT NULL` | Limite de tolerância superior permitido (+mm). |
| `tolerancia_neg` | `REAL` | `NOT NULL` | Limite de tolerância inferior permitido (-mm). |
| `meas_1` | `REAL` | `NOT NULL` | Primeira leitura bruta coletada na máquina de medir por coordenadas (CMM). |
| `meas_2` | `REAL` | `NOT NULL` | Segunda leitura bruta de confirmação coletada na CMM. |
| `valor_obtidomean` | `REAL` | `NOT NULL` | Média aritmética calculada a partir das leituras brutas (`meas_1` e `meas_2`) coletadas na MMC (mean - média). |
| `erro_calculado` | `REAL` | `NOT NULL` | Desvio/Erro dimensional apurado (`valor_obtidomean - valor_nominal`). |
| `status_resultado` | `TEXT` | `CHECK`, `NOT NULL` | Decisão de conformidade metrológica (`APROVADO` ou `REPROVADO`). |