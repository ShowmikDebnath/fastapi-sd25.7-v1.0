from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


db_url = "postgresql://showmik@localhost:5432/showmik25.7_v1.0"
engine = create_engine(db_url)
session = sessionmaker(autoflush=False, autocommit=False, bind=engine)

