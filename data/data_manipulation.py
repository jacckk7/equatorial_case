import math
import pandas as pd

import data.vetor as vt

df = pd.DataFrame(vt.data)

# Trata os dados referentes a datas

df["DATA_SIMPLES"] = pd.to_datetime(df["DATA_SIMPLES"], errors="coerce")
df["CONCLUSAO_DATA"] = pd.to_datetime(df["CONCLUSAO_DATA"], errors="coerce")

# Criar flag que determina se uma nota foi executada ou não

df["EXECUTADA"] = df["CONCLUSAO_DATA"].notna().astype(int)

# Cálculo da urgência dependendo se está no prazo ou fora do prazo

mapa_urgencia = {
    "FORA_PRAZO": 3,
    "NO_PRAZO": 1
}

df["URGENCIA"] = df["STATUS_PRAZO"].map(mapa_urgencia).fillna(1)

# Cálculo do score de prioridade

df["SCORE"] = df["DEBITO"] * df["URGENCIA"] * (1 / (df["FTR"] + 1))

# Cálculo da execução geral e por regional

execucao_geral = df["EXECUTADA"].mean() * 100
execucao_regional = df.groupby("REGIONAL2")["EXECUTADA"].mean() * 100

print(f"Taxa de execução geral: {execucao_geral:.2f}%\n")

print("Execução por regional:")
print(execucao_regional)

# Capacidade diária por regional

capacidades = {
    "LESTE": 15,
    "NORTE": 18,
    "SUL": 18,
    "OESTE": 12
}

# Alocação diária por regional

alocacao_final = []

for regiao, capacidade in capacidades.items():
    # filtra apenas notas da região
    filtro_regiao = df[df["REGIONAL2"] == regiao]

    # ordena por score (descendente)
    filtro_regiao = filtro_regiao.sort_values("SCORE", ascending=False)

    # agrupa por dia
    for dia, grupo in filtro_regiao.groupby("DATA_SIMPLES"):
        selecionadas = grupo.head(capacidade)
        alocacao_final.append(selecionadas)

# une tudo
alocacao_final = pd.concat(alocacao_final)

print("\nAlocação diária respeitando capacidade:")
print(alocacao_final[["DATA_SIMPLES", "REGIONAL2", "DEBITO", "FTR", "URGENCIA", "SCORE"]])

alocacao_final.to_csv("data/alocacao_final.csv", index=False)

# Total de pendências por regional

pendentes_por_regional = alocacao_final["REGIONAL2"].value_counts()

# Utilização da capacidade (pendentes / capacidade)

utilizacao = {
    regiao: pendentes_por_regional.get(regiao, 0) / capacidades[regiao]
    for regiao in capacidades
}

resultado_dias = []

for regiao, qtd in pendentes_por_regional.items():
    cap = capacidades.get(regiao, 0)
    if cap == 0:
        dias = None
    else:
        dias = math.ceil(qtd / cap)

    resultado_dias.append({
        "REGIONAL": regiao,
        "PENDENTES": qtd,
        "CAPACIDADE_DIARIA": cap,
        "DIAS_NECESSARIOS": dias
    })

dias_df = pd.DataFrame(resultado_dias)

print("\nDias necessários para concluir todas as pendências:")
print(dias_df)

# Transformar tudo em DataFrame para gráficos

df_exec = execucao_regional.reset_index()
df_exec.columns = ["Regional", "Execucao"]

df_backlog = pendentes_por_regional.reset_index()
df_backlog.columns = ["Regional", "Pendentes"]

df_util = pd.DataFrame(
    [(r, utilizacao[r]) for r in utilizacao],
    columns=["Regional", "Utilizacao"]
)
