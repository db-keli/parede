from sqlmodel import create_engine, Session, SQLModel
eng = 'database.db'

sqlite_url = f'sqlite:///{eng}'
engine = create_engine(sqlite_url, echo=True)
session = Session(bind=engine)

SQLModel.metadata.create_all(engine)