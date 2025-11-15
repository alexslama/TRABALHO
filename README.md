# UNLOGIC FÁBRICA ESPACIAL
### Sistema Didático de Gestão de Peças em Python

Este projeto foi desenvolvido como parte do desafio **Algoritmos e Lógica de Programação – UniFECAF**, aplicando conceitos fundamentais de tomada de decisão, modularidade, funções e estruturas de dados em Python.

O objetivo é simular um processo real de **inspeção, validação e armazenamento de peças industriais**, utilizando regras de qualidade pré-definidas e organização automática em caixas.

---

## 1. Objetivo do Sistema

O programa realiza:

- Cadastro de peças (ID, peso, cor, comprimento)
- Verificação automática dos critérios de qualidade:
  - Peso: 95 a 105 g
  - Cor: azul ou verde
  - Comprimento: 10 a 20 cm
- Armazenamento das peças aprovadas
- Fechamento automático da caixa ao atingir 10 peças aprovadas
- Listagem de peças aprovadas e reprovadas
- Remoção de peças por ID
- Relatório geral da produção

---

## 2. Tecnologias Utilizadas

- Python 3.x
- Execução via terminal (WSL, macOS ou Windows)
- Nenhuma biblioteca externa é necessária

---

## 3. Como Executar o Projeto (macOS, Windows e Linux)

### 1. Clonar ou baixar o repositório
git clone https://github.com/alexslama/TRABALHO

### 2. Navegar até a pasta do projeto
cd TRABALHO

### 3. Executar o programa
python3 UNLOGIC_FABRICA_ESPACIAL.py

Se estiver no Windows:
python UNLOGIC_FABRICA_ESPACIAL.py

---

## 4. Estrutura do Menu

1 - Cadastrar peça  
2 - Listar peças  
3 - Remover peça  
4 - Ver caixas fechadas  
5 - Gerar relatório final  
0 - Sair  

---

## 5. Exemplos de Entrada e Saída

### Exemplo 1 — Peça aprovada
Entrada:
ID da peça: P001
Peso: 100
Cor: azul
Comprimento: 15

Saída:
Peça aprovada e armazenada.

---

### Exemplo 2 — Peça reprovada (peso)
Entrada:
ID da peça: P002
Peso: 120
Cor: verde
Comprimento: 12

Saída:
Peça reprovada. Motivo: Peso fora do padrão

---

### Exemplo 3 — Caixa completada
Após cadastrar 10 peças aprovadas:

Peça aprovada e armazenada.
Caixa completa enviada.

---

### Exemplo 4 — Remover peça
Entrada:
ID da peça para remover: P001

Saída:
Peça removida com sucesso.

---

### Exemplo 5 — Relatório final
Relatório Final

Total de peças aprovadas: 7  
Total de peças reprovadas: 3  
Caixas fechadas: 0  
Peças na caixa atual: 7  

Motivos das reprovações:
- P005: Cor inválida
- P007: Peso fora do padrão
- P009: Comprimento fora do padrão

---

## 6. Estrutura Lógica do Programa

Entrada → Processamento → Validação → Armazenamento → Relatório

- Funções para modularizar tarefas
- Condicionais para validação de qualidade
- Listas para armazenar peças e caixas
- Laços de repetição para o menu interativo

---

## 7. Desafios e Benefícios

Benefícios:
- Organização clara do fluxo
- Código simples e fácil de manter
- Simulação fiel de processos industriais reais

Desafios:
- Controle da lógica de fechamento da caixa
- Tratamento de reprovações
- Manutenção da simplicidade

---

## 8. Expansão Futura

- Sensores IoT para leitura real de peso, cor e tamanho
- IA para identificar defeitos automaticamente
- Dashboard visual com gráficos em tempo real
- Banco de dados para histórico de produção

---

## 9. Autor

Alex Ernest Slama  
UniFECAF — Sistemas de IA e Automação  
2025
