from flask import Response, request
from routes import flaskRoutes

app = flaskRoutes()

######### Inicia execução do Flask API #########
if __name__ == "__main__":
    app.run(debug=True)