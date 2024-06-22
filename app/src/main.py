from flask import Flask, Response, request
import json
from model.categoria import Categoria
from controller.gerenciarCategoria import listarCategoria, listarCategorias, inserirCategoria, editarCategoria, deletarCategoria
from controller.gerenciarAnimal import listarAnimal, listarAnimais, inserirAnimal, editarAnimal, deletarAnimal

app = Flask(__name__)

###### Categoria ######

# listar categoria
@app.route('/categoria/<id>', methods=['GET'])
def listarUmaCategoria(id):
    try:
        lista = listarCategoria(id)
        if lista == None:
            return geraResponse(400, "Categoria", {}, "Categoria não encontrada")
        else:
            listarJson = lista.to_json()
            return geraResponse(200, "Categoria", listarJson)
    except Exception as error:
        print(error)
        return geraResponse(400, "Categoria", {}, "Erro ao listar categorias")

# listar categorias
@app.route('/categorias', methods=['GET'])
def listarTodasCategorias():
    try:
        lista = listarCategorias()
        listaJson = [item.to_json() for item in lista]
        return geraResponse(200, "Categorias", listaJson)
    except Exception as error:
        print(error)
        return geraResponse(400, "Categoria", {}, "Erro ao listar categorias")
    
# inserir nova categoria
@app.route('/categoria', methods=['POST'])
def inserirNovaCategoria():
    try:
        body = request.get_json()
        categoria = Categoria(nome=body["nome"])
        inserirCategoria(categoria)
        return geraResponse(201, "Categoria", categoria.to_json(), "Categoria inserida com sucesso")
    except Exception as error:
        print(error)
        return geraResponse(400, "Categoria", {}, "Erro ao inserir")

# editar uma categoria
@app.route('/categoria/<id>', methods=['PUT'])
def editarUmaCategoria(id):
    try:
        categoria = listarCategoria(id)
        body = request.get_json()
        if('nome' in body):
            categoria.nome = body['nome']
            editarCategoria(categoria)
        return geraResponse(200, "Categoria", categoria.to_json(), "Categoria editada com sucesso")
    except Exception as error:
        print(error)
        return geraResponse(400, "Categoria", {}, "Erro ao editar categoria")

# deletar uma categoria
@app.route('/categoria/<id>', methods=['DELETE'])
def deletarUmaCategoria(id):
    try:
        categoria = listarCategoria(id)
        deleta = deletarCategoria(categoria)
        if deleta:
            return geraResponse(200, "Categoria", categoria.to_json(), "Categoria deletada com sucesso")
        else:
            return geraResponse(400, "Categoria", categoria.to_json(), "Categoria não existe ou está vinculada à um animal")
    except Exception as error:
        print(error)
        return geraResponse(400, "Categoria", {}, "Erro ao deletar categoria")

# Gera resposta em json para o usuario
def geraResponse(status, nomeConteudo, conteudo, mensagem=False):
    body = {}
    body[nomeConteudo] = conteudo
    if(mensagem):
        body["mensagem"] = mensagem
    return Response(json.dumps(body), status=status, mimetype="application/json")

# Inicia execução do Flask API
if __name__ == "__main__":
    app.run()