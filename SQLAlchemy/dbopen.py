from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

class SessionCreater:
    def makeSession():
        engine = create_engine("mysql://root:root@localhost:3306/testdb")
        SessionClass = sessionmaker(engine)
        session = SessionClass()
        return session
