from flask import Flask

def flaskRoutes():
    app = Flask(__name__)

    from .usuario.usuario import bp as usuario_bp
    app.register_blueprint(usuario_bp, url_prefix='/usuario')

    from .produto.produto import bp as produto_bp
    app.register_blueprint(produto_bp, url_prefix='/produto')

    return app
