# UNLOGIC FÁBRICA ESPACIAL

Projeto simples em Python para gerenciar cadastro e validação de peças (exercício didático).

Funcionalidades
- Cadastrar peça (ID, peso, cor, comprimento).
- Validar qualidade (peso 95–105 g, cor azul/verde, comprimento 10–20 cm).
- Armazenar peças aprovadas numa caixa; quando a caixa atingir 10 peças, conta como caixa enviada.
- Listar todas as peças (com status e motivo de reprovação).
- Remover peça por ID.
- Ver caixas enviadas e gerar relatório com totais.

Requisitos
- Python 3.x instalado (Mac já vem com Python; se necessário: https://www.python.org).

Como rodar (Mac)
1. Abra o Terminal.
2. Entre na pasta do projeto:
   cd "/Users/unlogicrecords/Documents/ALGORITMOS"
3. Certifique-se do nome do arquivo principal. Recomenda-se:
   UNLOGIC_FABRICA_ESPACIAL.py
   (Se o seu arquivo atual contém `#` ou espaços especiais, renomeie:)
   mv "# UNLOGIC FÁBRICA ESPACIAL.py" UNLOGIC_FABRICA_ESPACIAL.py
4. Execute:
   python3 UNLOGIC_FABRICA_ESPACIAL.py

Uso (resumo)
- Menu interativo com opções: Cadastrar, Listar, Remover, Caixas, Relatório, Sair.
- Ao cadastrar, informe ID, peso (g), cor e comprimento (cm).
- Peças aprovadas vão para a caixa atual; ao atingir 10 peças, a caixa é considerada enviada.

Observações
- Nenhuma biblioteca externa necessária.
- Entrada numérica aceita vírgula ou ponto (ex: `100,5` ou `100.5`).
- IDs duplicados não são permitidos (o sistema atual pode rejeitar duplicatas).
- Se ocorrer erro ao rodar, copie a mensagem de erro e abra uma issue/contato para suporte.

Licença
- Uso educacional / pessoal.
