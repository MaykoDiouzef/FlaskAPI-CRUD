from flask import Response, request
from routes import flaskRoutes

app = flaskRoutes()

# Inicia execução do Flask API
if __name__ == "__main__":
    app.run(debug=True)


# #################

# from flask import Flask, Response, request
# import json
# from model.dao.usuario import Usuario
# from model.dto.usuario import listarUsuario, listarUsuarios, inserirUsuario, editarUsuario, deletarUsuario
# from model.dao.produto import Produto
# from model.dto.produto import listarProduto, listarProdutos, inserirProduto, editarProduto, deletarProduto

# app = Flask(__name__)

# ####################################################################

# ###### Categoria ######

# # listar usuario
# @app.route('/usuario/<id>', methods=['GET'])
# def listarUmUsuario(id):
#     try:
#         lista = listarUsuario(id)
#         if lista == None:
#             return geraResponse(400, "Usuario", {}, "Usuario não encontrado")
#         else:
#             listarJson = lista.to_json()
#             return geraResponse(200, "Usuario", listarJson)
#     except Exception as error:
#         print(error)
#         return geraResponse(400, "Usuario", {}, "Erro ao listar usuarios")

# # listar usuarios
# @app.route('/usuarios', methods=['GET'])
# def listarTodosUsuarios():
#     try:
#         lista = listarUsuarios()
#         listaJson = [item.to_json() for item in lista]
#         return geraResponse(200, "Usuarios", listaJson)
#     except Exception as error:
#         print(error)
#         return geraResponse(400, "Usuario", {}, "Erro ao listar usuarios")
    
# # inserir nova usuario
# @app.route('/usuario', methods=['POST'])
# def inserirNovaUsuario():
#     try:
#         body = request.get_json()
#         usuario = Usuario(nome=body["nome"])
#         inserirUsuario(usuario)
#         return geraResponse(201, "Usuario", usuario.to_json(), "Usuario inserida com sucesso")
#     except Exception as error:
#         print(error)
#         return geraResponse(400, "Usuario", {}, "Erro ao inserir")

# # editar uma usuario
# @app.route('/usuario/<id>', methods=['PUT'])
# def editarUmaUsuario(id):
#     try:
#         usuario = listarUsuario(id)
#         body = request.get_json()
#         if('nome' in body):
#             usuario.nome = body['nome']
#             editarUsuario(usuario)
#         return geraResponse(200, "Usuario", usuario.to_json(), "Usuario editada com sucesso")
#     except Exception as error:
#         print(error)
#         return geraResponse(400, "Usuario", {}, "Erro ao editar usuario")

# # deletar uma usuario
# @app.route('/usuario/<id>', methods=['DELETE'])
# def deletarUmaUsuario(id):
#     try:
#         usuario = listarUsuario(id)
#         deleta = deletarUsuario(usuario)
#         if deleta:
#             return geraResponse(200, "Usuario", usuario.to_json(), "Usuario deletada com sucesso")
#         else:
#             return geraResponse(400, "Usuario", usuario.to_json(), "Usuario não existe ou está vinculada à um produto")
#     except Exception as error:
#         print(error)
#         return geraResponse(400, "Usuario", {}, "Erro ao deletar usuario")
    

# ####################################################################


# # listar um produto
# @app.route('/produto/<id>', methods=['GET'])
# def listarUmProduto(id):
#     try:
#         lista = listarProduto(id)
#         if lista == None:
#             return geraResponse(400, "Produto", {}, "Produto não encontrado")
#         else:
#             listarJson = lista.to_json()
#             return geraResponse(200, "Produto", listarJson)
#     except Exception as error:
#         print(error)
#         return geraResponse(400, "Produto", {}, "Erro ao listar o produto")

# # listar produtos
# @app.route('/produtos', methods=['GET'])
# def listarTodosProdutos():
#     try:
#         lista = listarProdutos()
#         listaJson = [item.to_json() for item in lista]
#         return geraResponse(200, "Produtos", listaJson)
#     except Exception as error:
#         print(error)
#         return geraResponse(400, "Produtos", {}, "Erro ao listar produtos")

# # inserir novo produto
# @app.route('/produto', methods=['POST'])
# def inserirNovoProduto():
#     try:
#         body = request.get_json()
#         produto = Produto(usuarioId=body["usuarioId"], nome=body["nome"], sexo=body["sexo"], idade=body["idade"])
#         inserirProduto(produto)
#         return geraResponse(201, "Produto", {}, "Produto inserido com sucesso")
#         # return geraResponse(201, "Produto", produto.to_json(), "Produto inserido com sucesso")
#     except Exception as error:
#         print(error)
#         return geraResponse(400, "Produto", {}, "Erro ao inserir novo produto")
    

# ####################################################################


# # Gera resposta em json para o usuario
# def geraResponse(status, nomeConteudo, conteudo, mensagem=False):
#     body = {}
#     body[nomeConteudo] = conteudo
#     if(mensagem):
#         body["mensagem"] = mensagem
#     return Response(json.dumps(body), status=status, mimetype="application/json")

# # Inicia execução do Flask API
# if __name__ == "__main__":
#     app.run(debug=True)