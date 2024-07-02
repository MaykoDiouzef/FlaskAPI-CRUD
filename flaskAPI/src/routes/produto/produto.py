import json
from flask import Blueprint, Response, request
from config.auth import auth
from model.dto.produto import Produto
from model.dao.produto import listarProduto, listarProdutos, inserirProduto, editarProduto, deletarProduto

bp = Blueprint('produto', __name__)

######### inserir novo produto #########
@bp.route('/produto', methods=['POST'])
@auth.login_required
def inserirNovoProduto():
    try:
        body = request.get_json()
        produto = Produto(usuarioId=body["usuarioId"], nome=body["nome"])
        inserirProduto(produto)
        return geraResponse(201, "Produto", {}, "Produto inserido com sucesso")
    except Exception as error:
        return geraResponse(400, "Produto", {}, f"Erro ao inserir novo produto: {error}")

######### listar um produto #########
@bp.route('/produto/<id>', methods=['GET'])
@auth.login_required
def listarUmProduto(id):
    try:
        lista = listarProduto(id)
        if lista == None:
            return geraResponse(400, "Produto", {}, "Produto não encontrado")
        else:
            listarJson = lista.to_json()
            return geraResponse(200, "Produto", listarJson)
    except Exception as error:
        return geraResponse(400, "Produto", {}, f"Erro ao listar o produto: {error}")

######### listar produtos #########
@bp.route('/produtos', methods=['GET'])
@auth.login_required
def listarTodosProdutos():
    try:
        lista = listarProdutos()
        listaJson = [item.to_json() for item in lista]
        return geraResponse(200, "Produtos", listaJson)
    except Exception as error:
        return geraResponse(400, "Produtos", {}, f"Erro ao listar produtos: {error}")

######### editar um produto #########
@bp.route('/produto/<id>', methods=['PUT'])
@auth.login_required
def editarUmProduto(id):
    try:
        body = request.get_json()
        if('nome' in body):
            nome = body['nome']
            produto = editarProduto(id, nome)
            if produto:
                return geraResponse(200, "Produto", produto.to_json(), "Produto editado com sucesso")
            else:
                return geraResponse(400, "Produto", {}, f"Produto de {id} não existe")
        else:
            return geraResponse(400, "Produto", {}, "Informe nome do produto corretamente")
    except Exception as error:
        return geraResponse(400, "Produto", {}, f"Erro ao editar produto: {error}")

######### deletar um produto #########
@bp.route('/produto/<id>', methods=['DELETE'])
@auth.login_required
def deletarUmProduto(id):
    try:
        deleta = deletarProduto(id)
        if deleta:
            return geraResponse(200, "Produto", {}, "Produto deletado com sucesso")
        elif deleta == False:
            return geraResponse(400, "Produto", {}, f"Produto de {id} não existe")
        else:
            return geraResponse(400, "Produto", {}, "Erro ao deletar produto")
    except Exception as error:
        return geraResponse(400, "Produto", {}, f"Erro ao deletar produto: {error}")

######### Gera resposta em json para o usuário #########
def geraResponse(status, nomeConteudo, conteudo, mensagem=False):
    body = {}
    body[nomeConteudo] = conteudo
    if(mensagem):
        body["mensagem"] = mensagem
    return Response(json.dumps(body), status=status, mimetype="application/json")