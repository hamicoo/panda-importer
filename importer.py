import pandas as pd
import psycopg2

df = pd.read_excel('branch.xlsx')
df.columns = [c.lower() for c in df.columns] #postgres doesn't like capitals or spaces

from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:123@localhost:5432/postgres')
df.to_sql("tej_branch", engine)
