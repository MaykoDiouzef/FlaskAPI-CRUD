from connection.connection import Session
from model.dao.usuario import Usuario
from model.dao.produto import Produto

def inserirUsuario(usuario):
    session = Session()
    novaUsuario = Usuario(nome=usuario.nome)
    session.add(novaUsuario)
    session.commit()
    session.close()
    return novaUsuario

def listarUsuario(id):
    session = Session()
    usuario = session.query(Usuario).filter(Usuario.id==id).first()
    session.close()
    return usuario

def listarUsuarios():
    session = Session()
    usuario = session.query(Usuario).all()
    session.close()
    return usuario

def editarUsuario(usuario):
    session = Session()
    session.query(Usuario).filter(Usuario.id==usuario.id).update({"nome": usuario.nome})
    session.commit()
    session.close()
    return True

def deletarUsuario(id):
    aux = listarUsuario(id)
    if aux == None:
        return None
    else:
        verifica = buscarDeletar(id)
        if verifica:
            return False
        else:
            session = Session()
            session.query(Usuario).filter(Usuario.id==id).delete()
            session.commit()
            session.close()
            return True

def buscarDeletar(usuarioId):
    session = Session()
    usuario = session.query(Produto).filter(Produto.usuarioId==usuarioId).first()
    session.close()
    if usuario:
        return True
    else:
        return False