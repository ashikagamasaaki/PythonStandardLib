from db.dbopen import SessionCreater
from db.dbengine import User
from sqlalchemy_select import getFilterUser

def getSession():
    session = SessionCreater.makeSession()
    return session

def userDelete(user_id: int, last_name: str):
    session = getSession()
    del_user = session.query(User).filter(User.user_id == user_id).first()
    session.delete(del_user)
    session.commit()
    session.close()
    

if __name__ == '__main__':
    
    before_del_datas = getFilterUser(10001)
    for before_del_data in before_del_datas:
        print(f'Before Delete User ... user_id: {before_del_data.user_id}, first_name: {before_del_data.first_name}, last_name: {before_del_data.last_name}')
    
    userDelete(10001, 'Misaka')
    
    after_del_datas = getFilterUser(10001)
    for after_del_data in after_del_datas:
        print(f'After Delete User ... user_id: {after_del_data.user_id}, first_name: {after_del_data.first_name}, last_name: {after_del_data.last_name}')
    