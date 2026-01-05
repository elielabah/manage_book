from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine=create_engine(url="sqlite:///database.db",pool_pre_ping=True)
sessionLocal=sessionmaker(bind=engine)

def yield_session():
    session=sessionLocal()
    yield session