from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Entidades
class Categoria(Base):
    __tablename__ = "categoria"

    id = Column(Integer, primary_key=True)
    nome = Column(String, default="Tipo de categoria não informada")

    def __repr__(self):
        return f"[id:{self.id}, nome:{self.nome}]"