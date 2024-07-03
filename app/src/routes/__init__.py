from flask import Flask

######### Mapeia as rotas #########
def flaskRoutes():
    app = Flask(__name__)

    ######### Rotas Usuário #########
    from .usuario.usuario import bp as usuario_bp
    app.register_blueprint(usuario_bp, url_prefix='/usuario')

    ######### Rotas Produto #########
    from .produto.produto import bp as produto_bp
    app.register_blueprint(produto_bp, url_prefix='/produto')

    ######### Retorna as rotas #########
    return app