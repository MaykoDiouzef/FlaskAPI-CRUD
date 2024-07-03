import json
from flask import Blueprint, Response, jsonify, request
from config.auth import auth
from model.dto.usuario import Usuario
from model.dao.usuario import listarUsuario, listarUsuarios, inserirUsuario, editarUsuario, deletarUsuario

bp = Blueprint('usuario', __name__)

######### inserir novo produto #########
@bp.route('/usuario', methods=['POST'])
@auth.login_required
def inserirNovoUsuario():
    try:
        body = request.get_json()
        usuario = Usuario(nome=body["nome"])
        inserirUsuario(usuario)
        return geraResponse(201, "Usuario", usuario.to_json(), "Usuario inserido com sucesso")
    except Exception as error:
        return geraResponse(400, "Usuario", {}, f"Erro ao inserir: {error}")

######### listar um produto #########
@bp.route('/usuario/<id>', methods=['GET'])
@auth.login_required
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

######### listar produtos #########
@bp.route('/usuarios', methods=['GET'])
@auth.login_required
def listarTodosUsuarios():
    try:
        lista = listarUsuarios()
        listaJson = [item.to_json() for item in lista]
        return geraResponse(200, "Usuarios", listaJson)
    except Exception as error:
        return geraResponse(400, "Usuario", {}, f"Erro ao listar usuarios: {error}")

######### editar um produto #########
@bp.route('/usuario/<id>', methods=['PUT'])
@auth.login_required
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

######### deletar um produto #########
@bp.route('/usuario/<id>', methods=['DELETE'])
@auth.login_required
def deletarUmUsuario(id):
    try:            
        deleta = deletarUsuario(id)
        if deleta: ######### True #########
            return geraResponse(200, "Usuario", {}, "Usuario deletado com sucesso")
        elif deleta == False: ######### False #########
            return geraResponse(400, "Usuario", {}, "Usuario está vinculado à um produto")
        else: ######### None #########
            return geraResponse(400, "Usuario", {}, "Usuario não existe")
    except Exception as error:
        return geraResponse(400, "Usuario", {}, f"Erro ao deletar usuario: {error}")

######### Gera resposta em json para o usuário #########
def geraResponse(status, nomeConteudo, conteudo, mensagem=False):
    body = {}
    body[nomeConteudo] = conteudo
    if(mensagem):
        body["mensagem"] = mensagem
    return Response(json.dumps(body), status=status, mimetype="application/json")