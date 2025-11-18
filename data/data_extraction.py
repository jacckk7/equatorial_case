import openpyxl
import pandas as pd

#Leitura e obtenção de dados da planilha

wb = openpyxl.load_workbook("data/ESTUDO DE CASO_PRODUTIVIDADE CORTE.xlsx")
sheet = wb.active

data = []
count = 0

for row in sheet.iter_rows(values_only=True):
    if count == 0:
        count += 1
        continue
    
    new_line = {
        'EQUIPE 2': row[0],
        'TX_EQ_TIPONOTA': row[1],
        'TX_EQ_CODE': row[2],
        'FTR': row[3],
        'DEBITO': row[4],
        'GP': row[5],
        'REGIONAL2': row[6],
        'BASE': row[7],
        'SERVICOS_AGRUPADOS': row[8],
        'DATA_SIMPLES': row[9],
        'BALDE_SERVICO': row[10],
        'ABRAG': row[11],
        'CAUSA': row[12],
        'DT_LIMITE': row[13],
        'STATUS_PRAZO': row[14],
        'NOTA2': row[15],
        'TIPO_EQUIPE': row[16],
        'TURNO': row[17],
        'PERIMETRO': row[18],
        'HORA CONC': row[19],
        'FERRAMENTAS': row[20],
        'HOJE': row[21],
        'PERIODO': row[22],
        'TIPO_CORTE': row[23],
        'DIA': row[24],
        'CONCLUSAO_DATA': row[25],
    }

    data.append(new_line)


# Salva os dados extraídos em um arquivo Python

with open('data/vetor.py', "w", encoding="utf-8") as arquivo:
    arquivo.write(f"import datetime\n\ndata = {repr(data)}\n")
