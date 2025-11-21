"""
SkillMatch2050 - Protótipo para 'Novas carreiras, novas tecnologias'
"""

import pandas as pd
import random
from datetime import datetime


# === Base de carreiras do futuro ===
CAREERS = [
    {"career": "Engenheiro de IA Ética", "tech": ["IA", "ML"], "human_skills": ["ética", "pensamento crítico"], "impact": 9},
    {"career": "Especialista em Robótica Colaborativa", "tech": ["robótica", "IoT"], "human_skills": ["colaboração", "criatividade"], "impact": 8},
    {"career": "Gestor de Requalificação", "tech": ["e-learning", "plataformas"], "human_skills": ["didática", "empatia"], "impact": 7},
    {"career": "Curador de Dados Sustentáveis", "tech": ["big data", "cloud"], "human_skills": ["consciência ambiental", "governança"], "impact": 8},
    {"career": "Designer de Experiências Híbridas", "tech": ["UX", "AR/VR"], "human_skills": ["criatividade", "colaboração"], "impact": 7},
    {"career": "Analista de Impacto Social de Tech", "tech": ["analytics", "IA"], "human_skills": ["empatia", "ética"], "impact": 9}
]


# === Entrada do usuário ===
def collect_user_profiles():
    profiles = []
    print("=== Coleta de perfis para recomendações (digite 'fim' para encerrar) ===")

    while True:
        name = input("Nome (ou 'fim'): ").strip()
        if name.lower() == "fim":
            break

        skills = input("Skills atuais (ex: comunicação,python): ").strip()
        tech_interest = input("Interesse em tecnologia (IA, robótica...) ou 'qualquer': ").strip()

        while True:
            try:
                availability = int(input("Disponibilidade para requalificação (1-5): "))
                if 1 <= availability <= 5:
                    break
                else:
                    print("Digite um número entre 1 e 5.")
            except:
                print("Valor inválido.")

        profiles.append({
            "name": name,
            "skills": [s.strip().lower() for s in skills.split(",") if s.strip()],
            "tech_interest": [t.strip() for t in tech_interest.split(",")] if tech_interest.lower() != "qualquer" else [],
            "availability": availability
        })

        print(f"Perfil de {name} adicionado.\n")

    return profiles


# === Função dentro de função + cálculo de score ===
def score_fit(profile, career):

    def _skill_overlap(user, needed):
        return len(set(user).intersection({s.lower() for s in needed}))

    human_overlap = _skill_overlap(profile["skills"], career["human_skills"])

    tech_bonus = 0
    if profile["tech_interest"]:
        if any(t.lower() in [c.lower() for c in career["tech"]] for t in profile["tech_interest"]):
            tech_bonus = 2

    availability_score = profile["availability"] / 5
    impact = career["impact"] / 10

    score = (human_overlap * 1.5) + tech_bonus + (availability_score * 2) + (impact * 3)
    return min(100, int(score * 10))


# === Repetição + Condições ===
def recommend_careers_for_profile(profile, top_n=3):
    scored = []

    for c in CAREERS:
        s = score_fit(profile, c)
        scored.append({
            "career": c["career"],
            "score": s,
            "tech": c["tech"],
            "impact": c["impact"]
        })

    scored_sorted = sorted(scored, key=lambda x: x["score"], reverse=True)

    recommendations = []
    for item in scored_sorted[:top_n]:
        if item["score"] < 40:
            note = "Recomenda-se curso introdutório."
        elif item["score"] < 70:
            note = "Boa compatibilidade — focar requalificação específica."
        else:
            note = "Excelente compatibilidade — seguir plano avançado."

        recommendations.append({**item, "note": note})

    return recommendations


# DataFrame 
def build_dataframe(profiles, recs):
    rows = []

    for prof, rec_list in zip(profiles, recs):
        for r in rec_list:
            rows.append({
                "name": prof["name"],
                "skills": ", ".join(prof["skills"]),
                "availability": prof["availability"],
                "recommended_career": r["career"],
                "score": r["score"],
                "note": r["note"],
                "tech_required": ", ".join(r["tech"]),
                "timestamp": datetime.utcnow().isoformat()
            })

    df = pd.DataFrame(rows)
    return df.sort_values(by="score", ascending=False).reset_index(drop=True)


# Saída
def generate_report(df, save_csv=False):
    print("\n=== RELATÓRIO FINAL ===")
    
    if df.empty:
        print("Nenhum dado encontrado.")
        return

    top = df.head(10)

    for _, row in top.iterrows():
        print(f"{row['name']} → {row['recommended_career']} (score {row['score']}) — {row['note']}")

    print("\nCarreiras mais recomendadas:")
    print(df.groupby("recommended_career")["name"].count().sort_values(ascending=False))

    if save_csv:
        df.to_csv("skillmatch_report.csv", index=False)
        print("\nArquivo salvo como 'skillmatch_report.csv'.")


# Main
def main():
    print("SkillMatch2050 — Recomendações de carreiras do futuro\n")

    profiles = collect_user_profiles()

    if not profiles:
        print("Nenhum perfil informado — gerando exemplos automáticos.\n")
        example_skills = [
            ["comunicação", "ética"],
            ["python", "estatistica"],
            ["design", "colaboração"],
            ["gestão", "empatia"]
        ]
        for i in range(4):
            profiles.append({
                "name": f"Aluno_{i+1}",
                "skills": example_skills[i],
                "tech_interest": random.choice([["IA"], ["robótica"], ["AR/VR"], []]),
                "availability": random.randint(2, 5)
            })

    all_recs = []
    for p in profiles:
        all_recs.append(recommend_careers_for_profile(p))

    df = build_dataframe(profiles, all_recs)

    save = input("Salvar relatório em CSV? (s/n): ").lower()
    generate_report(df, save_csv=(save == "s"))

    show = input("Mostrar DataFrame completo? (s/n): ").lower()
    if show == "s":
        print(df.to_string(index=False))


if __name__ == "__main__":
    main()
