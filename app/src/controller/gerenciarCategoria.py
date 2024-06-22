from connection.connection import Session
from model.categoria import Categoria
from model.animal import Animal

def listarCategoria(id):
    session = Session()
    categoria = session.query(Categoria).filter(Categoria.id==id).first()
    session.close()
    return categoria

def listarCategorias():
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
    return novaCategoria

def editarCategoria(categoria):
    session = Session()
    session.query(Categoria).filter(Categoria.id==categoria.id).update({"nome": categoria.nome})
    session.commit()
    session.close()
    return True 

def deletarCategoria(categoria):
    verifica = buscarDeletar(categoria.id)
    if verifica:
        return False
    else:
        session = Session()
        session.query(Categoria).filter(Categoria.id==categoria.id).delete()
        session.commit()
        session.close()
        return True

def buscarDeletar(categoriaId):
    session = Session()
    categoria = session.query(Animal).filter(Animal.categoriaId==categoriaId).first()
    session.close()
    if categoria:
        return True
    else:
        return False