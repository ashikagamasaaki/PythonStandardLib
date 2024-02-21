from dbengine import User
from dbopen import SessionCreater

test_user = User(user_id='10002', first_name='Hanako', last_name='Yamada', age=24)

session = SessionCreater.makeSession()
session.add(test_user)
session.commit()
session.close()