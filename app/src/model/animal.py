from sqlalchemy import Column, String, Integer, BigInteger, ForeignKey
from sqlalchemy.orm import relationship
from model.categoria import Base

# Entidades
class Animal(Base):
    __tablename__ = "animal"

    id = Column(Integer, primary_key=True)
    categoriaId = Column(Integer, ForeignKey("categoria.id"))
    nome = Column(String, default="Não informado")
    sexo = Column(String, default="Não Informado")
    idade = Column(Integer, default=0)
    categoria = relationship("Categoria", lazy="subquery")
    
    def __repr__(self):
        return f"[id:{self.id}, categoria:{self.categoria}, nome:{self.nome}, sexo:{self.sexo}, idade:{self.idade}]"