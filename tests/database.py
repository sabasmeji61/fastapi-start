from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.main import app
from app import schemas
from app.config import settings
from app.database import get_db
from app.database import Base
from alembic import command

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:pgadmin4@localhost:5432/fastapi_test'
# SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#def override_get_db():
#    db = TestingSessionLocal()
#    try:
#        yield db
#    finally:
#        db.close()

# client = TestClient(app)  ## line replaced by  def client()

@pytest.fixture  # (scope="function") or (scope="module")
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture  # (scope="function")
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = override_get_db
    # Base.metadata.drop_all(bind=engine)
    # Base.metadata.create_all(bind=engine)
    yield TestClient(app)
    # run our code after our test finishes

