# 06 - DOCUMENTAÇÃO TÉCNICA DO MVP - PARTE 1

## 1. Introdução

O presente documento apresenta a implementação inicial do sistema de controle de calibrações do laboratório de metrologia da Schulz S.A., desenvolvido como parte da AV03 do Projeto Aplicado I.

A implementação utiliza a linguagem Python e os conceitos de Programação Orientada a Objetos (POO), com o objetivo de representar as principais entidades do sistema e automatizar as regras de negócio relacionadas aos processos de medição e validação de tolerâncias.

## 2. Objetivo

O objetivo desta etapa é implementar as classes de domínio `Tecnico`, `Equipamento` e `Medicao`, organizando os dados e comportamentos necessários para representar os processos de calibração.

Também foram desenvolvidos e executados testes para verificar o funcionamento dos cálculos metrológicos, incluindo o cálculo da média das medições, a apuração do erro dimensional e a validação dos limites de tolerância de forma defensiva e automatizada.


## 3. Conceitos de Programação Orientada a Objetos (POO)

O sistema foi desenvolvido utilizando conceitos de Programação Orientada a Objetos (POO), organizando os dados e comportamentos em classes que representam as entidades do laboratório de metrologia.

### 3.1 Classes

Foram implementadas três classes principais:

- **Tecnico:** representa os profissionais responsáveis pela execução das medições.
- **Equipamento:** representa os instrumentos e dispositivos submetidos aos processos de calibração.
- **Medicao:** representa os registros dos ensaios e contém os métodos responsáveis pelos cálculos e pela validação dos resultados.

### 3.2 Atributos

Os atributos são as características que armazenam as informações de cada objeto.

Principais atributos utilizados no projeto:

- **Tecnico:** `id_tecnico`, `matricula`, `nome` e `turno`.
- **Equipamento:** `id_equipamento`, `tag_codigo`, `descricao` e `setor_cliente`.
- **Medicao:** `id_medicao`, `id_equipamento_fk`, `id_tecnico_fk`, `numero_certificado`, `data_calibracao`, `parametro_cota`, `valor_nominal`, `tolerancia_pos`, `tolerancia_neg`, `meas_1`, `meas_2`, `valor_obtidomean`, `erro_calculado` e `status_resultado`.

### 3.3 Construtor (__init__)

O método construtor `__init__` é utilizado para inicializar os objetos com os valores recebidos durante sua criação.

Nas classes `Tecnico`, `Equipamento` e `Medicao`, esse método atribui os valores recebidos aos respectivos atributos utilizando a palavra-chave `self`. O identificador de cada entidade é opcional na criação do objeto, permitindo que seja posteriormente preenchido pelo banco de dados SQLite.

Na classe `Medicao`, o construtor invoca automaticamente os métodos internos de cálculo no momento da instanciação, garantindo a imediata consistência dos valores metrológicos obtidos.

### 3.4 Métodos

Os métodos representam os comportamentos das classes.

Na classe `Medicao` foram implementados:

- `calcular_media()`: calcula a média aritmética das duas leituras (`meas_1` e `meas_2`).
- `calcular_erro()`: calcula a diferença entre a média obtida e o valor nominal.
- `validar_tolerancia()`: verifica defensivamente se o erro calculated está dentro dos limites de tolerância (utilizando valores absolutos para garantir consistência de sinal), retornando `APROVADO` ou `REPROVADO`.


## 4. Diagrama UML das Classes

O diagrama abaixo representa a estrutura das três classes implementadas no sistema, seus principais atributos e métodos.

```mermaid
classDiagram
    class Tecnico {
        +id_tecnico
        +matricula
        +nome
        +turno
    }

    class Equipamento {
        +id_equipamento
        +tag_codigo
        +descricao
        +setor_cliente
    }

    class Medicao {
        +id_medicao
        +id_equipamento_fk
        +id_tecnico_fk
        +numero_certificado
        +data_calibracao
        +parametro_cota
        +valor_nominal
        +tolerancia_pos
        +tolerancia_neg
        +meas_1
        +meas_2
        +valor_obtidomean
        +erro_calculado
        +status_resultado
        +calcular_media()
        +calcular_erro()
        +validar_tolerancia()
    }

    Tecnico "1" --> "0..*" Medicao : executa
    Equipamento "1" --> "0..*" Medicao : possui


## 5. Testes e Validação das Regras de Negócio

Foram desenvolvidos testes individuais para verificar a criação e o funcionamento das classes `Tecnico`, `Equipamento` e `Medicao`.

### 5.1 Testes da classe Medicao

Foram realizados dois testes para verificar o cálculo da média, a apuração do erro dimensional e a validação dos limites de tolerância.

**Teste 1 - Resultado APROVADO**

- **Valor nominal:** 10,00 mm
- **Primeira medição:** 10,04 mm
- **Segunda medição:** 10,06 mm
- **Média calculada:** 10,05 mm
- **Erro calculado:** 0,05 mm
- **Resultado:** APROVADO

O resultado foi aprovado porque o erro calculado permaneceu dentro dos limites de tolerância estabelecidos.

**Teste 2 - Resultado REPROVADO**

- **Valor nominal:** 10,00 mm
- **Primeira medição:** 10,20 mm
- **Segunda medição:** 10,20 mm
- **Média calculada:** 10,20 mm
- **Erro calculated:** 0,20 mm
- **Resultado:** REPROVADO

O resultado foi reprovado porque o erro calculated ultrapassou o limite superior de tolerância de 0,10 mm.

### 5.2 Resultado dos testes

Os testes demonstraram que os métodos implementados na classe `Medicao` realizam corretamente os cálculos e identificam a conformidade ou não conformidade das medições conforme os limites de tolerância definidos.

Os resultados obtidos confirmaram o funcionamento das regras de negócio implementadas nesta etapa do MVP.


## 6. Organização dos Arquivos do Projeto

O projeto foi organizado em arquivos separados, seguindo o princípio de separação de responsabilidades.

### 6.1 Classes de domínio

As classes foram armazenadas na pasta `models`:

- `models/tecnico.py`: implementação da classe `Tecnico`.
- `models/equipamento.py`: implementação da classe `Equipamento`.
- `models/medicao.py`: implementação da classe `Medicao` e suas regras de cálculo e validação.

### 6.2 Arquivos de teste

Foram criados arquivos específicos para verificar o funcionamento das classes e do banco de dados:

### 6.2 Arquivos de teste

Foram criados arquivos específicos para verificar o funcionamento das classes e a integridade da camada de persistência:

- `teste_tecnico.py`: teste de instanciação e atributos da classe `Tecnico`.
- `teste_equipamento.py`: teste de instanciação e atributos da classe `Equipamento`.
- `teste_medicao.py`: teste dos cálculos metrológicos (média, erro) e validação de limites de tolerância.
- `teste_classes.py`: verificação da importação modular e instanciação em conjunto das classes de domínio.
- `teste_database.py`: validação do ciclo de vida completo dos dados (**CRUD**) e integridade referencial do SQLite, testando a criação de tabelas, inserção defensiva (**Create**), consulta estruturada com relacionamentos (**Read** via `INNER JOIN`), atualização de status (**Update**) e exclusão de registros (**Delete**).

A separação dos arquivos facilita a manutenção, a organização e a realização de testes individuais durante o desenvolvimento.


## 7. Higienização da estrutura do projeto

O `.gitignore` foi configurado para garantir a higiene e a segurança do repositório, impedindo o rastreamento desnecessário de arquivos temporários compilados pelo Python (como as pastas `__pycache__` e extensões `.pyc`). Com a exclusão dessas pastas do controle de versão e do ambiente remoto, o repositório mantém apenas o código-fonte essencial, otimizando o tamanho do projeto e evitando conflitos em execuções locais de diferentes colaboradores.


## 8. Versionamento semântico

Foi implementado com o uso de **Git Tags**, permitindo rastrear formalmente a evolução histórica do sistema desde as etapas iniciais até a consolidação do MVP. O histórico conta com marcos de desenvolvimento (`v0.1.0` a `v0.3.0`) registrando a criação da estrutura de arquivos, das classes de domínio e do banco SQLite, culminando na versão estável `v1.0.1`, que sela a entrega do MVP Parte 1 com todas as regras metrológicas e de repositório devidamente ajustadas.


## 9. Conclusão

Nesta etapa do projeto, foram desenvolvidas as classes `Tecnico`, `Equipamento` e `Medicao`, utilizando os conceitos de Programação Orientada a Objetos em Python.

Também foram implementadas as regras de negócio relacionadas aos cálculos metrológicos, incluindo o cálculo da média das medições, a apuração do erro dimensional e a validação dos resultados conforme os limites de tolerância estabelecidos.

Os testes realizados demonstraram que o sistema consegue identificar corretamente medições aprovadas e reprovadas, contribuindo para a confiabilidade dos resultados e a rastreabilidade dos processos de calibração.

Dessa forma, a implementação da primeira parte do MVP estabelece a base lógica necessária para a continuidade do desenvolvimento e a integração com o banco de dados.