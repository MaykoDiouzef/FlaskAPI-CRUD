from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from model.dto.usuario import Base

######### Criação da classe produto #########
class Produto(Base):
    __tablename__ = "produto"

    ######### Atributos #########
    id = Column(Integer, primary_key=True)
    usuarioId = Column(Integer, ForeignKey("usuario.id"))
    nome = Column(String, default="Não informado")
    usuario = relationship("Usuario", lazy="subquery")
    
    ######### Padrão da mensagem de retorno para o usuário #########
    def to_json(self):
        return {"id":self.id, "usuario":{"id":self.usuario.id, "nome":self.usuario.nome}, "nome":self.nome}