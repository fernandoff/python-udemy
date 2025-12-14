from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///banco.db", echo=True)
Base = declarative_base()

class Filme(Base):
    __tablename__= "filmes"
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)
    nota = Column(Float, nullable=False)
    
Base.metadata.create_all(engine)

# Inserir dados
def adiciona_filme(nome, ano, nota):
    session = sessionmaker(bind=engine)
    session = session()
    filme = Filme(nome=nome, ano=ano, nota=nota)
    session.add(filme)
    session.commit()
    session.close()

# adiciona_filme("Mario", 2022, 9.5)
# adiciona_filme("Sonic", 2019, 8.5)

# Atualizar dados
def atualiza_filme(id, nome=None, ano=None, nota=None):
    session = sessionmaker(bind=engine)
    session = session()
    filme = session.query(Filme).filter_by(id=id).first()
    if filme:
        if nome is not None:
            filme.nome = nome
        if ano is not None:
            filme.ano = ano
        if nota is not None:
            filme.nota = nota
        session.commit()
    session.close()

# atualiza_filme(1, "Homem Aranha", 2016, 9.0)

# Excluir dados
def exclui_filme(id):
    session = sessionmaker(bind=engine)
    session = session()
    filme = session.query(Filme).filter_by(id=id).first()
    if filme:
        session.delete(filme)
        
    session.commit()
    session.close()

exclui_filme(2)
        
