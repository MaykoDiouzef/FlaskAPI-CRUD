from config.connection import Session
from model.dto.usuario import Usuario
from model.dto.produto import Produto

######### Insert no bando de dados #########
def inserirUsuario(usuario):
    session = Session()
    novaUsuario = Usuario(nome=usuario.nome)
    session.add(novaUsuario)
    session.commit()
    session.close()
    return novaUsuario

######### Select Where no bando de dados #########
def listarUsuario(id):
    session = Session()
    usuario = session.query(Usuario).filter(Usuario.id==id).first()
    session.close()
    return usuario

######### Select All no bando de dados #########
def listarUsuarios():
    session = Session()
    usuario = session.query(Usuario).all()
    session.close()
    return usuario

######### Update Where no bando de dados #########
def editarUsuario(usuario):
    session = Session()
    session.query(Usuario).filter(Usuario.id==usuario.id).update({"nome": usuario.nome})
    session.commit()
    session.close()
    return True

######### Delete Where no bando de dados #########
def deletarUsuario(id):
    usuario = listarUsuario(id)
    ######### Verifica se existe usuário #########
    if usuario:
        ######### Verifica se usuário é vinculado em um produto #########
        session = Session()
        verifica = session.query(Produto).filter(Produto.usuarioId==id).first()
        session.close()
        ######### Se for vinculado, não faz nada #########
        if verifica:
            return False
        else:
            ######### Se não for vinculado, deleta #########
            session = Session()
            session.query(Usuario).filter(Usuario.id==usuario.id).delete()
            session.commit()
            session.close()
            return True
    else:
        ######### Não existe usuário #########
        return None