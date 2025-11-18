# Equatorial Case

Este projeto realiza a extração de dados de uma planilha Excel (`ESTUDO DE CASO_PRODUTIVIDADE CORTE.xlsx`), converte cada linha em um dicionário Python e salva os dados em um arquivo de texto (`data.txt`). Após isso é possível fazer a manipulação dos dados para se extrair insights.

## Funcionalidades
- Leitura de planilha Excel com o pacote `openpyxl`.
- Conversão de cada linha da planilha em um dicionário Python.
- Salvamento dos dados extraídos em um arquivo `data.txt` (um dicionário por linha).
- Leitura do arquivo `data.txt` para popular a variável `data` com os dicionários.

## Pré-requisitos
- Python 3.8 ou superior
- `openpyxl` instalado

## Instalação
1. Clone este repositório:
   ```bash
   git clone <url-do-repositorio>
   cd equatorial_case
   ```
2. (Opcional) Crie e ative um ambiente virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Instale as dependências:
   ```bash
   pip install openpyxl
   pip install pandas
   pip install dash==2.15.0
   pip install plotly==5.22.0
   ```

## Como executar
1. Para extrair os dados da planilha e gerar o `data.txt`, execute:
   ```bash
   python data_extraction.py
   ```
   O arquivo `data.txt` será criado com os dados extraídos.

2. Para ler o arquivo `data.txt` e popular a variável `data` com os dicionários, execute o `main.py`.

## Observações
- O arquivo `data.txt` armazena cada registro como um dicionário em uma linha.
- O script utiliza `ast.literal_eval` para converter as linhas do arquivo de texto em dicionários Python.
- Certifique-se de que o arquivo Excel está no formato esperado, com as colunas corretas.

## Licença
Este projeto é apenas para fins de estudo.
