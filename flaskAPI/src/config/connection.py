from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

######### Declaração de variaveis de configurações de conexão #########
# "dialect+driver://user:password@host/dbname"
# "mariadb+pymysql://root:123456789@localhost:3309/db-flask"

dialect = "mariadb"
driver = "pymysql"
user = "root"
password = "123456789"
host = "localhost"
port = "3309"
dbname = "db-flask"

######### Conexão ao banco de dados #########
engine = create_engine(f"{dialect}+{driver}://{user}:{password}@{host}:{port}/{dbname}")
Session = sessionmaker(bind=engine)