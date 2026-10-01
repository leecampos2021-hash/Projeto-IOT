# Pipeline de Dados com IoT e Docker

Projeto desenvolvido para a disciplina de **Disruptive Architectures: IoT, Big Data e IA**.

O projeto consiste na criação de um **pipeline de dados** capaz de realizar a leitura de dados de temperatura de dispositivos IoT, armazená-los em um banco de dados **PostgreSQL utilizando Docker** e disponibilizar informações para análise por meio de um **dashboard desenvolvido com Streamlit**.

---

## Tecnologias utilizadas

- **Python**
- **Pandas**
- **SQLAlchemy**
- **PostgreSQL**
- **Docker**
- **Streamlit**
- **Plotly**
- **Psycopg2**
- **Git e GitHub**

---

## Estrutura do projeto

```text
Projeto-IOT/
│
├── docs/
│   └── README.md
│
├── src/
│   ├── data/
│   │   └── IOT-temp.csv/
│   │       └── IOT-temp.csv
│   │
│   ├── sql/
│   │   └── views.sql
│   │
│   ├── app.py
│   └── dashboard.py
│
└── venv/
```

---

## Fonte dos dados

Foi utilizado o conjunto de dados **Temperature Readings: IoT Devices**, disponibilizado pelo Kaggle.

O conjunto contém leituras de temperatura de dispositivos IoT.

**Fonte:**  
https://www.kaggle.com/datasets/atulanandjha/temperature-readings-iot-devices

---

## Funcionamento do pipeline

O pipeline segue as seguintes etapas:

1. **Leitura do arquivo CSV** utilizando Pandas.
2. **Conexão com o PostgreSQL** utilizando SQLAlchemy e Psycopg2.
3. **Inserção dos dados** na tabela `leituras`.
4. **Criação de views SQL** para facilitar a consulta e análise dos dados.
5. **Consulta das views** pelo dashboard.
6. **Visualização dos dados** utilizando Streamlit e Plotly.

---

## Fluxo do projeto

```text
Arquivo CSV
    ↓
Python + Pandas
    ↓
SQLAlchemy + Psycopg2
    ↓
PostgreSQL
    ↓
Views SQL
    ↓
Streamlit + Plotly
    ↓
Dashboard
```

---

## Configuração do ambiente

É necessário ter instalado:

- **Python**
- **Docker**
- **Git**

Foi utilizado um **ambiente virtual Python** para instalar as dependências do projeto.

### Criação do ambiente virtual

```bash
python -m venv venv
```

### Ativação no PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

### Instalação das dependências

```bash
pip install pandas psycopg2-binary sqlalchemy streamlit plotly
```

---

## PostgreSQL com Docker

O banco de dados **PostgreSQL** foi executado utilizando um container Docker.

### Criação do container

```bash
docker run --name postgres-iot -e POSTGRES_PASSWORD=sua_senha -p 5432:5432 -d postgres
```

Após a criação do container, o PostgreSQL fica disponível na **porta 5432**.

### Verificação do container

Para verificar se o container está em execução:

```bash
docker ps
```

Caso o container já exista, mas esteja parado:

```bash
docker start postgres-iot
```

---

## Inserção dos dados

O arquivo `app.py` realiza a leitura do CSV e insere os dados na tabela `leituras` do PostgreSQL.

### Execução

```bash
python app.py
```

Após a execução, é exibida a mensagem:

```text
Dados inseridos com sucesso!
```

---

## Views SQL

Foram criadas **views no PostgreSQL** para facilitar a análise dos dados.

### 1. Temperatura média por ambiente

A view `temperatura_media_por_ambiente` calcula a temperatura média registrada em cada ambiente.

```sql
CREATE VIEW temperatura_media_por_ambiente AS
SELECT
    "room_id/id",
    AVG(temp) AS temperatura_media
FROM leituras
GROUP BY "room_id/id";
```

### 2. Temperatura máxima e mínima por ambiente

A view `temp_max_min_ambiente` apresenta os valores mínimo e máximo de temperatura registrados em cada ambiente.

```sql
CREATE VIEW temp_max_min_ambiente AS
SELECT
    "room_id/id",
    MIN(temp) AS mínima,
    MAX(temp) AS máxima
FROM leituras
GROUP BY "room_id/id"
ORDER BY "room_id/id";
```

### 3. Quantidade de entradas e saídas

A view `entradas_saidas` contabiliza a quantidade de registros classificados como entrada (`In`) e saída (`Out`).

```sql
CREATE VIEW entradas_saidas AS
SELECT
    "out/in",
    COUNT(*) AS quantidade
FROM leituras
GROUP BY "out/in";
```

---

## Dashboard

O dashboard foi desenvolvido utilizando **Streamlit e Plotly**.

Ele apresenta:

- **Temperatura média por ambiente**
- **Temperaturas mínima e máxima por ambiente**
- **Quantidade de entradas e saídas**

### Execução do dashboard

```bash
streamlit run dashboard.py
```

Após executar o comando, o **Streamlit disponibilizará o dashboard localmente**.

---

## Visualizações

### Temperatura média por ambiente

![Temperatura média por ambiente](imagens/temperatura-media-ambiente.png)

### Temperaturas mínima e máxima por ambiente

![Temperaturas mínima e máxima](imagens/grafico-min-max.png)

### Quantidade de entradas e saídas

![Entradas e saídas](imagens/grafico-entradas-saidas.png)

---

## Principais resultados

Os dados armazenados no PostgreSQL foram utilizados para gerar **indicadores de temperatura e movimentação**.

A análise permite observar:

- **A temperatura média registrada nos ambientes**
- **Os valores mínimos e máximos de temperatura**
- **A quantidade de registros de entrada e saída**

Essas informações podem ser utilizadas como base para o **acompanhamento de ambientes monitorados por dispositivos IoT**.

---

## Comandos Git utilizados

### Inicialização do repositório

```bash
git init
```

### Adição dos arquivos

```bash
git add .
```

### Criação do commit

```bash
git commit -m "Projeto inicial: Pipeline de Dados IoT"
```

### Envio para o GitHub

```bash
git push
```

---

## Conclusão

O projeto demonstra a construção de um **pipeline de dados utilizando Python, Docker, PostgreSQL e Streamlit**.

Os dados de temperatura são coletados a partir de um arquivo CSV, armazenados em um banco PostgreSQL e posteriormente consultados por meio de **views SQL**.

O **Streamlit** permite apresentar os resultados de forma visual e interativa.