from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, String, Integer
from common import Base, logger
from flask_login import UserMixin

class User(UserMixin, Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    f_name = Column(String)
    l_name = Column(String)
    email  = Column(String)

    def set_password(self, password):
        self.password =  generate_password_hash(password, method="sha256")
    
    def check_password(self, password):
        return check_password_hash(self.password, password)

    @staticmethod
    def query(session, mode="read", user_id=None, username=None):
        if mode == "query":
            if user_id:
                return session.query(User).filter(User.id == user_id)
            else:
                users = session.query(User)

                if username:
                    users = users.filter(User.username == username)
                
                return users

        else:
            return session.query(User)
