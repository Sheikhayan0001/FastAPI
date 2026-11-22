#===========================================================================================================================
#                                               CONNECTING DATABASE 
#===========================================================================================================================
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# postgresql://username:password@localhost/blogdb

DATABASE_URL = "postgresql://postgres:POSTGRES_DB@2006@localhost/blogdb"

engine = create_engine(DATABASE_URL)

# for opr useful.
SessionLocal = sessionmaker(bind=engine)

# for using model
Base = declarative_base()