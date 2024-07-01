from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from model.dao.usuario import Base

# Entidades
class Produto(Base):
    __tablename__ = "produto"

    id = Column(Integer, primary_key=True)
    usuarioId = Column(Integer, ForeignKey("usuario.id"))
    nome = Column(String, default="Não informado")
    usuario = relationship("Usuario", lazy="subquery")
    
    def to_json(self):
        return {"id":self.id, "usuario":{"id":self.usuario.id, "nome":self.usuario.nome}, "nome":self.nome}