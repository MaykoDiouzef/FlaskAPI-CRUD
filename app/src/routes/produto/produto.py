import json
from flask import Blueprint, Response, request
from model.dao.produto import Produto
from model.dto.produto import listarProduto, listarProdutos, inserirProduto, editarProduto, deletarProduto

bp = Blueprint('produto', __name__)

### inserir novo produto ###
@bp.route('/produto', methods=['POST'])
def inserirNovoProduto():
    try:
        body = request.get_json()
        produto = Produto(usuarioId=body["usuarioId"], nome=body["nome"])
        inserirProduto(produto)
        return geraResponse(201, "Produto", {}, "Produto inserido com sucesso")
    except Exception as error:
        return geraResponse(400, "Produto", {}, f"Erro ao inserir novo produto: {error}")

### listar um produto ###
@bp.route('/produto/<id>', methods=['GET'])
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

### listar produtos ###
@bp.route('/produtos', methods=['GET'])
def listarTodosProdutos():
    try:
        lista = listarProdutos()
        listaJson = [item.to_json() for item in lista]
        return geraResponse(200, "Produtos", listaJson)
    except Exception as error:
        return geraResponse(400, "Produtos", {}, f"Erro ao listar produtos: {error}")

### editar um produto ###
@bp.route('/produto/<id>', methods=['PUT'])
def editarUmProduto(id):
    try:
        produto = listarProduto(id)
        body = request.get_json()
        if('nome' in body):
            produto.nome = body['nome']
            aux = editarProduto(produto)
            if aux:
                return geraResponse(200, "Produto", produto.to_json(), "Produto editado com sucesso")
            else:
                return geraResponse(400, "Produto", {}, "Erro ao editar produto")
        else:
            return geraResponse(400, "Produto", {}, "Erro ao editar produto")
    except Exception as error:
        return geraResponse(400, "Produto", {}, f"Erro ao editar produto: {error}")

### deletar um produto ###
@bp.route('/produto/<id>', methods=['DELETE'])
def deletarUmProduto(id):
    try:
        deleta = deletarProduto(id)
        if deleta:
            return geraResponse(200, "Produto", {}, "Produto deletado com sucesso")
        elif deleta == False:
            return geraResponse(400, "Produto", {}, "Produto não existe")
        else:
            return geraResponse(400, "Produto", {}, "Erro ao deletar produto")
    except Exception as error:
        return geraResponse(400, "Produto", {}, f"Erro ao deletar produto: {error}")

# Gera resposta em json para o usuario
def geraResponse(status, nomeConteudo, conteudo, mensagem=False):
    body = {}
    body[nomeConteudo] = conteudo
    if(mensagem):
        body["mensagem"] = mensagem
    return Response(json.dumps(body), status=status, mimetype="application/json")