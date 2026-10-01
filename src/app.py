import pandas as pd

from sqlalchemy import create_engine


df = pd.read_csv("data/IOT-temp.csv/IOT-temp.csv")

DATABASE_URL = "postgresql+psycopg2://postgres:123456@localhost:5432/postgres"
engine = create_engine(DATABASE_URL)

df.to_sql(
    "leituras",
    engine,
    if_exists="append",
    index=False
)

print("Dados inseridos com sucesso!")