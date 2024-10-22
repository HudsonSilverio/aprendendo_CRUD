# python aprendendo.py
from sqlalchemy import create_engine 

# 01. conectar ao SQlite em memoria

engine = create_engine('sqlite:///meubanco.db', echo=True)

print("conexao com SQLite estabelecida. ")

# 02. Codigos para abstrair o bando de dados para os objetos em py
from sqlalchemy.orm import declarative_base 
from sqlalchemy import Column, Integer, String

Base = declarative_base()

# 03. Criando a tabela 

class Usuario(Base):
    __tablename__ = "usuarios" # nome da tabela

# Cada linha desse codigo sera uma COLUNA na tabela
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)

# comando para criar as tabelas

Base.metadata.create_all(engine)

# 04. Adicionando informacoes dentro do banco de dados:

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

novo_usuario = Usuario(nome="regina", idade=53)
session.add(novo_usuario)
session.commit()

print("Usuario inserido com sucesso !")
# with Session () as session:
#     novo_usuario = Usuario(nome="tome", idade=21)
#     session.add(novo_usuario)


 #codigo usado para realizar querys dentro BD usando PY

usuario = session.query(Usuario).filter_by(nome="João").first()
print(f"Usuario encontrado: {usuario.nome}, Idade: {usuario.idade}")