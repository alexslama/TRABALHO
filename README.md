# UNLOGIC FÁBRICA ESPACIAL

**Sistema Didático de Gestão de Peças em Python**

Este projeto foi desenvolvido como parte do desafio da disciplina **Algoritmos e Lógica de Programação – UniFECAF**. O objetivo é simular um processo real de inspeção, validação e armazenamento de peças industriais, aplicando conceitos de decisão, modularidade, funções e estruturas de dados em Python.

---

## 🏭 Introdução

Automatizar tarefas industriais é essencial para elevar a eficiência, garantir padrões de qualidade e reduzir falhas humanas. Este sistema demonstra, de maneira prática, como a lógica de programação pode solucionar desafios reais de controle e organização em linhas de produção.

---

## 🎯 Objetivo do Sistema

O programa realiza:

- **Cadastro de peças** (ID, peso, cor, comprimento)
- **Validação automática** dos critérios de qualidade:
    - Peso: 95 a 105 g
    - Cor: azul ou verde
    - Comprimento: 10 a 20 cm
- **Armazenamento automático** das peças aprovadas em caixas de até 10 unidades
- **Fechamento automático** da caixa ao atingir 10 peças aprovadas
- **Listagem de peças** aprovadas e reprovadas com motivos das reprovações
- **Remoção de peças** por ID
- **Relatório final** detalhado de produção

---

## ⚙️ Tecnologias Utilizadas

- **Python 3.x**
- Execução via terminal (WSL, macOS ou Windows)
- Sem dependências externas (apenas bibliotecas padrão)

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
Certifique-se de que Python 3.x está instalado em seu sistema. Se não estiver, baixe em [python.org](https://python.org)

### Passos para Execução

1. **Clone ou baixe o repositório:**
   ```bash
   git clone https://github.com/alexslama/TRABALHO
   ```

2. **Acesse a pasta do projeto:**
   ```bash
   cd TRABALHO
   ```

3. **Execute o programa:**
   - **Linux/macOS:**
     ```bash
     python3 UNLOGIC_FABRICA_ESPACIAL.py
     ```
   - **Windows:**
     ```bash
     python UNLOGIC_FABRICA_ESPACIAL.py
     ```

---

## 📋 Estrutura do Menu

O sistema oferece um menu interativo com as seguintes opções:

```
1 - Cadastrar peça galáctica
   Descrição: Registrar e validar peça; armazena automaticamente se aprovada.

2 - Listar peças
   Descrição: Exibe todas as peças com status e motivos de reprovação.

3 - Remover peça do sistema
   Descrição: Remove registro de peça por ID.

4 - Ver caixas fechadas
   Descrição: Mostra caixas completas já enviadas (10 peças cada).

5 - Gerar relatório final
   Descrição: Resumo dos totais e motivos de reprovação.

0 - Encerrar missão
   Descrição: Sair do sistema.
```

---

## 💻 Exemplos de Uso

### Exemplo 1: Peça Aprovada

**Entrada:**
```
ID da peça: P001
Peso: 100
Cor: azul
Comprimento: 15
```

**Saída:**
```
✅ Peça aprovada e armazenada na caixa atual!
```

### Exemplo 2: Peça Reprovada (Peso Fora do Padrão)

**Entrada:**
```
ID da peça: P002
Peso: 120
Cor: verde
Comprimento: 12
```

**Saída:**
```
❌ Peça reprovada! Motivo: Peso fora dos padrões intergalácticos
```

### Exemplo 3: Caixa Completada (10 Peças Aprovadas)

**Entrada:**
Cadastrar 10 peças aprovadas consecutivamente.

**Saída:**
```
✅ Peça aprovada e armazenada na caixa atual!
📦 A caixa atingiu 10 peças e foi enviada para o Setor de Hyper-Transporte!
```

### Exemplo 4: Remover Peça

**Entrada:**
```
ID da peça para remover: P001
```

**Saída:**
```
Peça removida com sucesso do universo catalogado!
```

### Exemplo 5: Relatório Final

**Saída:**
```
📑 Relatório de Produção da UNLOGIC FÁBRICA ESPACIAL

Total de peças aprovadas: 7
Total de peças reprovadas: 3
Caixas fechadas enviadas: 0
Peças na caixa atual: 7

Motivos de reprovação:
- P005: Cor inválida
- P007: Peso fora do padrão
- P009: Comprimento fora do padrão
```

---

## 🧩 Estrutura Lógica

O sistema segue o fluxo:

**Entrada → Processamento → Validação → Armazenamento → Relatório**

Com implementação de:

- ✅ **Funções** para modularizar tarefas
- ✅ **Condicionais** para validação dos critérios
- ✅ **Listas** para armazenamento de peças e caixas
- ✅ **Laços de repetição** para o menu interativo
- ✅ **Boas práticas** de documentação e legibilidade

---

## 🏆 Benefícios da Automação Digital

- **Eficiência operacional**: Reduz tempo de processamento manualmente
- **Organização clara**: Fluxo estruturado e fácil de acompanhar
- **Minimização de erros**: Validação automática e consistente
- **Rastreabilidade**: Relatório detalhado de todas as peças
- **Escalabilidade**: Código modular permite futuras expansões

---

## ⚡ Desafios e Aprendizados

### Desafios Enfrentados:
- Controle correto de fechamento das caixas ao atingir 10 unidades
- Tratamento automático e informativo das reprovações
- Manutenção da didática e simplicidade sem perder funcionalidade

### Aprendizados:
- Importância da validação de dados em tempo real
- Estrutura modular facilita manutenção futura
- Interface clara e descrições detalhadas melhoram experiência do usuário

---

## 🔮 Possibilidades de Expansão Futura

Este protótipo pode evoluir para:

- **Integração com IoT**: Sensores para leitura automática de peso, cor e tamanho
- **Inteligência Artificial**: Inspeção e previsão de defeitos
- **Dashboard Visual**: Gráficos em tempo real com tecnologias como Plotly ou Matplotlib
- **Banco de Dados**: PostgreSQL ou MongoDB para histórico de produção
- **API REST**: Integração com sistemas de gestão (ERP)
- **Exportação de Dados**: CSV, Excel ou JSON para análise avançada

---

## 👨‍💻 Autor

**Alex Ernest Slama**  
UniFECAF — Sistemas de IA e Automação  
2025

---

## 📄 Como Citar este Projeto

```
Slama, Alex Ernest. UNLOGIC Fábrica Espacial: Sistema Didático de Gestão de Peças em Python. 
UniFECAF, 2025. Disponível em: https://github.com/alexslama/TRABALHO
```

---

## 📞 Contato e Dúvidas

Para dúvidas ou sugestões, abra uma **Issue** no repositório ou entre em contato através da página do projeto no GitHub.

**Que a Força do Código esteja com você! 🚀**
