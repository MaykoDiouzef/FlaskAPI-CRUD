from connection.connection import Session
from model.categoria import Categoria

def listarCategoria():
    session = Session()
    categoria = session.query(Categoria).all()
    session.close()
    return categoria

def inserirCategoria(nome):
    session = Session()
    novaCategoria = Categoria(nome=nome)
    session.add(novaCategoria)
    session.commit()
    session.close()
    return True

def editarCategoria(id, nome):
    session = Session()
    session.query(Categoria).filter(Categoria.id==id).update({"nome": nome})
    session.commit()
    session.close()
    return True 

def deletarCategoria(id):
    session = Session()
    a = session.query(Categoria).filter(Categoria.id==id).delete()
    session.commit()
    session.close()
    return a