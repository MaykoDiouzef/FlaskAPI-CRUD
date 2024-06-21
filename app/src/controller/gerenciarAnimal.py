from connection.connection import Session
from model.categoria import Categoria
from model.animal import Animal

def listarAnimal():
    session = Session()
    animal = session.query(Animal).all()
    session.close()
    return animal

def inserirAnimal(nome, sexo, idade, categoriaId):
    session = Session()
    novoAnimal = Animal(nome=nome, sexo=sexo, idade=idade, categoriaId=categoriaId)
    session.add(novoAnimal)
    session.commit()
    session.close()
    return True

def editarAnimal(id, nome, sexo, idade, categoriaId):
    session = Session()
    session.query(Animal).filter(Animal.id==id).update({"nome":nome, "sexo":sexo, "idade":idade, "categoriaId":categoriaId})
    session.commit()
    session.close()
    return True

def deletarAnimal(id):
    session = Session()
    session.query(Animal).filter(Animal.id==id).delete()
    session.commit()
    session.close()
    return True

