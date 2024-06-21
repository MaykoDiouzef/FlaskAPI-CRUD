from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Configurações
engine = create_engine("mariadb+pymysql://root:123456789@localhost:3308/db")
Session = sessionmaker(bind=engine)