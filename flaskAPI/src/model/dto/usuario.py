from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

######### Base para reconhecimento do ORM #########
Base = declarative_base()

######### Criação da classe Usuario #########
class Usuario(Base):
    __tablename__ = "usuario"
    
    ######### Atributos #########
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, default="Usuario não informado")

    ######### Padrão da mensagem de retorno para o usuário #########
    def to_json(self):
        return {"id":self.id, "nome":self.nome}