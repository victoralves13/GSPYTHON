"""
FutureWork Network — Sistema simples de análise de perfis para o futuro do trabalho
Atende: entrada, saída, repetição, condição, funções, função interna e DataFrame.
"""

import pandas as pd
from datetime import datetime



# Coleta de perfis (entrada)

def coletar_perfis():
    perfis = []
    print("\n=== FutureWork Network — Cadastro de Perfis ===")

    while True:
        nome = input("Nome (ou 'fim' para encerrar): ").strip()
        if nome.lower() == "fim":
            break

        area = input("Área de interesse (tech, design, gestão, saúde): ").strip().lower()
        experiencia = input("Experiência (iniciante, médio, avançado): ").strip().lower()

        while True:
            try:
                dispo = int(input("Disponibilidade semanal (1 a 5): "))
                if 1 <= dispo <= 5:
                    break
                print("Use um valor entre 1 e 5.")
            except:
                print("Valor inválido.")

        perfis.append({
            "nome": nome,
            "area": area,
            "experiencia": experiencia,
            "dispo": dispo
        })

        print("Perfil registrado.\n")

    return perfis



# Mostrar perfis cadastrados

def mostrar_perfis(perfis):
    if not perfis:
        print("\nNenhum perfil cadastrado.")
        return

    print("\n=== Perfis Cadastrados ===")
    for p in perfis:
        print(f"- {p['nome']} | área: {p['area']} | exp: {p['experiencia']} | disp: {p['dispo']}")
    print("==========================\n")



# Classificação (com função interna)

def classificar(perfil):

    def peso_exp(nivel):
        if nivel == "iniciante": return 1
        if nivel == "médio" or nivel == "medio": return 2
        if nivel == "avançado" or nivel == "avancado": return 3
        return 1

    xp = peso_exp(perfil["experiencia"])
    disp = perfil["dispo"]

    area = perfil["area"]

    if area == "tech":
        trilha = "Programação / IA"
    elif area == "design":
        trilha = "UX / Design Digital"
    elif area == "gestão":
        trilha = "Liderança / Dados"
    elif area == "saúde":
        trilha = "Saúde Digital"
    else:
        trilha = "Descoberta de Perfil"

    score = xp * 2 + disp
    return trilha, score


# DataFrame

def montar_dataframe(perfis):
    dados = []

    for p in perfis:
        trilha, score = classificar(p)
        dados.append({
            "nome": p["nome"],
            "area": p["area"],
            "experiencia": p["experiencia"],
            "disponibilidade": p["dispo"],
            "trilha_sugerida": trilha,
            "score": score,
            "timestamp": datetime.now().isoformat()
        })

    df = pd.DataFrame(dados)
    return df.sort_values(by="score", ascending=False).reset_index(drop=True)


# Relatório final (saída)

def relatorio(df):
    print("\n=== Relatório FutureWork ===")

    for _, linha in df.head(5).iterrows():
        print(f"{linha['nome']} → {linha['trilha_sugerida']} (Score {linha['score']})")

    print("\nContagem por trilha:")
    print(df.groupby("trilha_sugerida")["nome"].count())



# Main

def main():
    perfis = coletar_perfis()

    if not perfis:
        print("Nenhum perfil inserido.")
        return

    ver = input("Mostrar perfis cadastrados? (s/n): ").lower()
    if ver == "s":
        mostrar_perfis(perfis)

    df = montar_dataframe(perfis)
    relatorio(df)

    salvar = input("\nSalvar como CSV? (s/n): ").lower()
    if salvar == "s":
        df.to_csv("futurework_network.csv", index=False)
        print("Arquivo salvo.")

    ver_df = input("Mostrar DataFrame completo? (s/n): ").lower()
    if ver_df == "s":
        print("\n", df.to_string(index=False))


if __name__ == "__main__":
    main()
