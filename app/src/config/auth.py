from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

######### usuario e senha de acesso a API #########
users = {
    "aluno": generate_password_hash("123"),
}

######### verificaçaõ de usuario e senha de acesso a API #########
@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username
    return None