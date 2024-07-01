from connection.connection import Session
from model.dao.usuario import Usuario
from model.dao.produto import Produto

def inserirProduto(produto):
    session = Session()
    novoProduto = Produto(usuarioId=produto.usuarioId, nome=produto.nome)
    session.add(novoProduto)
    session.commit()
    session.close()
    return novoProduto

def listarProduto(id):
    session = Session()
    produto = session.query(Produto).filter(Produto.id==id).first()
    session.close()
    return produto

def listarProdutos():
    session = Session()
    produto = session.query(Produto).all()
    session.close()
    return produto

def editarProduto(id, nome, usuarioId):
    session = Session()
    session.query(Produto).filter(Produto.id==id).update({"nome":nome, "usuarioId":usuarioId})
    session.commit()
    session.close()
    return True

def deletarProduto(id):
    produto = listarProduto(id)
    if produto == None:
        return False
    else:
        session = Session()
        session.query(Produto).filter(Produto.id==produto.id).delete()
        session.commit()
        session.close()
        return True