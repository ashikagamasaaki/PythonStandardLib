from db.dbengine import User
from db.dbopen import SessionCreater

def getSession():
    session = SessionCreater.makeSession()
    return session


def getAllUser():
    session = getSession()
    users = session.query(User).all()
    session.close()
    return users


def getFilterUser(user_id):
    session = getSession()
    user = session.query(User).\
        filter(User.user_id == user_id).\
        all()
    session.close()
    return user


if __name__ == '__main__':
    users = getAllUser()
    for user in users:
        print(f'User ... user_id: {user.user_id}, first_name: {user.first_name}, last_name: {user.last_name}')
    
    
    filter_user = getFilterUser(10003)
    print(f'Filter User ... user_id: {user.user_id}, first_name: {user.first_name}, last_name: {user.last_name}')
