import json
from flask import Blueprint, Response, request
from model.dao.usuario import Usuario
from model.dto.usuario import listarUsuario, listarUsuarios, inserirUsuario, editarUsuario, deletarUsuario

bp = Blueprint('usuario', __name__)

### inserir novo usuario ###
@bp.route('/usuario', methods=['POST'])
def inserirNovoUsuario():
    try:
        body = request.get_json()
        usuario = Usuario(nome=body["nome"])
        inserirUsuario(usuario)
        return geraResponse(201, "Usuario", usuario.to_json(), "Usuario inserido com sucesso")
    except Exception as error:
        return geraResponse(400, "Usuario", {}, f"Erro ao inserir: {error}")

### listar um usuario ###
@bp.route('/usuario/<id>', methods=['GET'])
def listarUmUsuario(id):
    try:
        lista = listarUsuario(id)
        if lista == None:
            return geraResponse(400, "Usuario", {}, "Usuario não encontrado")
        else:
            listarJson = lista.to_json()
            return geraResponse(200, "Usuario", listarJson)
    except Exception as error:
        return geraResponse(400, "Usuario", {}, f"Erro ao listar usuarios: {error}")

### listar todos usuarios ###
@bp.route('/usuarios', methods=['GET'])
def listarTodosUsuarios():
    try:
        lista = listarUsuarios()
        listaJson = [item.to_json() for item in lista]
        return geraResponse(200, "Usuarios", listaJson)
    except Exception as error:
        return geraResponse(400, "Usuario", {}, f"Erro ao listar usuarios: {error}")

### editar um usuario ###
@bp.route('/usuario/<id>', methods=['PUT'])
def editarUmUsuario(id):
    try:
        usuario = listarUsuario(id)
        body = request.get_json()
        if('nome' in body):
            usuario.nome = body['nome']
            aux = editarUsuario(usuario)
            if aux:
                return geraResponse(200, "Usuario", usuario.to_json(), "Usuario editado com sucesso")
            else:
                return geraResponse(400, "Usuario", {}, "Erro ao editar usuario")
    except Exception as error:
        return geraResponse(400, "Usuario", {}, f"Erro ao editar usuario: {error}")

### deletar um usuario ###
@bp.route('/usuario/<id>', methods=['DELETE'])
def deletarUmUsuario(id):
    try:            
        deleta = deletarUsuario(id)
        if deleta:
            return geraResponse(200, "Usuario", {}, "Usuario deletado com sucesso")
        elif deleta == None:
            return geraResponse(400, "Usuario", {}, "Usuario não existe")
        else:
            return geraResponse(400, "Usuario", {}, "Usuario está vinculado à um produto")
    except Exception as error:
        return geraResponse(400, "Usuario", {}, f"Erro ao deletar usuario: {error}")


# Gera resposta em json para o usuario
def geraResponse(status, nomeConteudo, conteudo, mensagem=False):
    body = {}
    body[nomeConteudo] = conteudo
    if(mensagem):
        body["mensagem"] = mensagem
    return Response(json.dumps(body), status=status, mimetype="application/json")