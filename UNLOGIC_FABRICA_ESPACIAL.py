# ...existing code...
import os
# Listas principais
pecas = []               # Todas as peças cadastradas
caixas_fechadas = []     # Armazena caixas completas (10 peças aprovadas cada)
caixa_atual = []         # Caixa em uso

# Função para limpar tela (funciona no VS Code)
def limpar_tela():
    """Limpa a tela do terminal (Windows ou Unix)."""
    os.system('cls' if os.name == 'nt' else 'clear')

# Regras de qualidade
def verificar_qualidade(peso, cor, comprimento):
    """
    Verifica se a peça atende aos padrões de qualidade.
    Retorna (True, "") se aprovada ou (False, motivo) se reprovada.
    Regras:
      - peso entre 95g e 105g
      - cor: azul ou verde
      - comprimento entre 10cm e 20cm
    """
    if peso < 95 or peso > 105:
        return False, "Peso fora dos padrões intergalácticos"
    if cor.lower() not in ["azul", "verde"]:
        return False, "Cor fora do padrão da Frota Estelar"
    if comprimento < 10 or comprimento > 20:
        return False, "Comprimento incompatível com encaixe galáctico"
    return True, ""

# Cadastrar peça
def cadastrar_peca():
    """
    Etapa: Cadastro de peça
    Descrição: Coleta dados da peça, valida pelas regras de qualidade,
    registra no sistema e, se aprovada, armazena na caixa atual.
    Se a caixa atingir 10 peças aprovadas, é fechada e enviada.
    """
    limpar_tela()
    print("🔧 Cadastro de Peça Galáctica\n")
    print("Descrição: Informe ID, peso, cor e comprimento. A peça será testada e armazenada se aprovada.\n")

    id_peca = input("ID da peça (ex: PLX-01): ")
    peso = float(input("Peso da peça (em gramas): "))
    cor = input("Cor da peça (azul ou verde): ")
    comprimento = float(input("Comprimento (em cm): "))

    aprovada, motivo = verificar_qualidade(peso, cor, comprimento)

    peca = {
        "id": id_peca,
        "peso": peso,
        "cor": cor,
        "comprimento": comprimento,
        "aprovada": aprovada,
        "motivo": motivo
    }

    pecas.append(peca)

    if aprovada:
        caixa_atual.append(peca)
        print("\n✅ Peça aprovada e armazenada na caixa atual!")
        if len(caixa_atual) == 10:
            caixas_fechadas.append(caixa_atual.copy())
            caixa_atual.clear()
            print("📦 A caixa atingiu 10 peças e foi enviada para o Setor de Hyper-Transporte!")
    else:
        print(f"\n❌ Peça reprovada! Motivo: {motivo}")

    input("\nPressione ENTER para voltar ao menu...")

# Listar peças
def listar_pecas():
    """
    Etapa: Listagem de peças
    Descrição: Exibe todas as peças cadastradas com seus status e motivos de reprovação.
    """
    limpar_tela()
    print("📋 Lista de Peças Cadastradas\n")
    
    if not pecas:
        print("Nenhuma peça cadastrada até o momento no sistema galáctico.")
    else:
        for p in pecas:
            status = "APROVADA" if p["aprovada"] else "REPROVADA"
            print(f"ID: {p['id']} | {status} | Peso: {p['peso']}g | Cor: {p['cor']} | Comp: {p['comprimento']}cm")
            if not p["aprovada"]:
                print(f"   Motivo da reprovação: {p['motivo']}")

    input("\nPressione ENTER para voltar ao menu...")

# Remover peça
def remover_peca():
    """
    Etapa: Remoção de peça
    Descrição: Remove uma peça do registro pelo seu ID (use com cuidado).
    """
    limpar_tela()
    print("🗑 Remover Peça do Sistema\n")
    print("Descrição: Informe o ID exato da peça a ser removida do sistema.\n")
    id_remove = input("Digite o ID da peça para remover: ")

    for p in pecas:
        if p["id"] == id_remove:
            pecas.remove(p)
            print("Peça removida com sucesso do universo catalogado!")
            break
    else:
        print("Nenhuma peça encontrada com esse ID no registro intergaláctico.")

    input("\nPressione ENTER para voltar ao menu...")

# Listar caixas fechadas
def listar_caixas():
    """
    Etapa: Visualizar caixas fechadas
    Descrição: Mostra as caixas já fechadas (cada uma com 10 peças aprovadas).
    """
    limpar_tela()
    print("📦 Caixas Galácticas Fechadas\n")
    print("Descrição: Exibe quantas caixas completas foram enviadas para transporte.\n")

    if not caixas_fechadas:
        print("Nenhuma caixa fechada ainda. Continue produzindo, cadete!")
    else:
        for i, caixa in enumerate(caixas_fechadas, start=1):
            print(f"Caixa {i} - Contém {len(caixa)} peças aprovadas.")

    input("\nPressione ENTER para voltar ao menu...")

# Relatório final
def gerar_relatorio():
    """
    Etapa: Relatório final
    Descrição: Gera um resumo da produção com totais de peças aprovadas/reprovadas,
    caixas enviadas e motivos de reprovação.
    """
    limpar_tela()
    print("📑 Relatório de Produção da UNLOGIC FÁBRICA ESPACIAL\n")
    print("Descrição: Resumo completo da produção para controle de qualidade.\n")

    aprovadas = sum(1 for p in pecas if p["aprovada"])
    reprovadas = sum(1 for p in pecas if not p["aprovada"])

    print(f"Total de peças aprovadas: {aprovadas}")
    print(f"Total de peças reprovadas: {reprovadas}")
    print(f"Caixas fechadas enviadas: {len(caixas_fechadas)}")
    print(f"Peças na caixa atual: {len(caixa_atual)}")

    print("\nMotivos de reprovação:")
    for p in pecas:
        if not p["aprovada"]:
            print(f"- {p['id']}: {p['motivo']}")

    input("\nPressione ENTER para voltar ao menu...")

# Menu principal
def menu():
    """
    Interface principal com descrições curtas de cada etapa.
    """
    while True:
        limpar_tela()
        print("===  UNLOGIC FÁBRICA ESPACIAL  ===")
        print("1 - Cadastrar peça galáctica")
        print("   Descrição: Registrar e validar peça; armazena automaticamente se aprovada.")
        print("2 - Listar peças")
        print("   Descrição: Exibe todas as peças com status e motivos de reprovação.")
        print("3 - Remover peça do sistema")
        print("   Descrição: Remove registro de peça por ID.")
        print("4 - Ver caixas fechadas")
        print("   Descrição: Mostra caixas completas já enviadas (10 peças cada).")
        print("5 - Gerar relatório final")
        print("   Descrição: Resumo dos totais e motivos de reprovação.")
        print("0 - Encerrar missão\n")

        opc = input("Escolha uma opção: ")

        if opc == "1":
            cadastrar_peca()
        elif opc == "2":
            listar_pecas()
        elif opc == "3":
            remover_peca()
        elif opc == "4":
            listar_caixas()
        elif opc == "5":
            gerar_relatorio()
        elif opc == "0":
            print("Encerrando sistema... Que a Força do Código esteja com você! 🚀")
            break
        else:
            print("Opção inválida na galáxia ou em qualquer outra dimensão!")
            input("Pressione ENTER...")

menu()
# ...existing code...