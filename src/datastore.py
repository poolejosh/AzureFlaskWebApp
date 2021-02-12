from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from common import Base
from flask_login import LoginManager
from models import User

login_manager = LoginManager()

engine = create_engine("sqlite:///data.db")
db_session = scoped_session(sessionmaker(
    autocommit=False, autoflush=False, bind=engine))

Base.query = db_session.query_property()

def init_db():
    # Drop & re-create all tables
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    test_user = User(username="test_user", f_name="test", l_name="user", email="test@user.com")
    test_user.set_password(password="password")
    db_session.add(test_user)
    db_session.commit()
