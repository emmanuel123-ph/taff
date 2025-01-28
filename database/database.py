from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db" # Utilisation d'une base SQLite
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:@localhost:3306/testdb"
#Test sur la base de données Mysql installé pip install pymysql
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread":
False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)