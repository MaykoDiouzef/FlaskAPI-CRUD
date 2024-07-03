from config.connection import Session
from model.dto.produto import Produto

######### Insert no bando de dados #########
def inserirProduto(produto):
    session = Session()
    novoProduto = Produto(usuarioId=produto.usuarioId, nome=produto.nome)
    session.add(novoProduto)
    session.commit()
    session.close()
    return novoProduto

######### Select Where no bando de dados #########
def listarProduto(id):
    session = Session()
    produto = session.query(Produto).filter(Produto.id==id).first()
    session.close()
    return produto

######### Select All no bando de dados #########
def listarProdutos():
    session = Session()
    produto = session.query(Produto).all()
    session.close()
    return produto

######### Update Where no bando de dados #########
def editarProduto(id, nome):
    ######### verifica de o produto existe #########
    produto = listarProduto(id)
    if produto == None:
        return False
    else:
        ######### produto encontrado #########
        produto.id = id
        produto.nome = nome
        session = Session()
        session.query(Produto).filter(Produto.id==produto.id).update({"nome":produto.nome})
        session.commit()
        session.close()
        return produto

######### Delete Where no bando de dados #########
def deletarProduto(id):
    ######### verifica de o produto existe #########
    produto = listarProduto(id)
    if produto == None:
        return False
    else:
        ######### produto encontrado #########
        session = Session()
        session.query(Produto).filter(Produto.id==produto.id).delete()
        session.commit()
        session.close()
        return True