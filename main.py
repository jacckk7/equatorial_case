import dash
from dash import html, dcc
import plotly.express as px

import data.data_manipulation as md

def semaforo_execucao(valor):
    if valor >= 90:
        return "green"
    elif valor >= 80:
        return "yellow"
    else:
        return "red"


app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Dashboard de Produtividade", style={"text-align": "center"}),

    # ---------------------
    # INDICADORES (CARDS)
    # ---------------------
    html.Div([
        html.Div([
            html.H3("Execução Geral"),
            html.H2(f"{md.execucao_geral:.2f}%", 
                    style={"color": semaforo_execucao(md.execucao_geral)})
        ], className="card"),

        html.Div([
            html.H3("Backlog Total"),
            html.H2(md.alocacao_final.shape[0])
        ], className="card"),

        html.Div([
            html.H3("Capacidade Total/Dia"),
            html.H2(sum(md.capacidades.values()))
        ], className="card"),
    ], className="row"),

    # ---------------------
    # GRÁFICO: Execução por regional
    # ---------------------
    dcc.Graph(
        figure=px.bar(md.df_exec, x="Regional", y="Execucao", 
                      title="Execução por Regional (%)",
                      color="Execucao",
                      color_continuous_scale=["red", "yellow", "green"])
    ),

    # ---------------------
    # GRÁFICO: backlog
    # ---------------------
    dcc.Graph(
        figure=px.bar(md.df_backlog, x="Regional", y="Pendentes",
                      title="Backlog por Regional")
    ),

    # ---------------------
    # GRÁFICO: Utilização da capacidade
    # ---------------------
    dcc.Graph(
        figure=px.bar(md.df_util, x="Regional", y="Utilizacao",
                      title="Utilização da Capacidade (pendentes / capacidade)")
    ),
])

if __name__ == "__main__":
    app.run_server(debug=True)

