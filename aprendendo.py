# python aprendendo.py
from sqlalchemy import create_engine 

#conectar ao SQlite em memoria

engine = create_engine('sqlite://meubanco.db', echo=True)

print("conexao com SQLite estabelecida. ")