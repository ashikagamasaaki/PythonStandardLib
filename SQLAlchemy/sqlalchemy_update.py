from db.dbopen import SessionCreater
from db.dbengine import User
from sqlalchemy_select import getFilterUser

def getSession():
    session = SessionCreater.makeSession()
    return session

def userUpdate(user_id: int, last_name: str):
    session = getSession()
    upd_user = session.query(User).filter(User.user_id == user_id).first()
    upd_user.last_name = last_name
    session.commit()
    session.close()
    

if __name__ == '__main__':
    
    before_upd_datas = getFilterUser(10001)
    for before_upd_data in before_upd_datas:
        print(f'Before Update User ... user_id: {before_upd_data.user_id}, first_name: {before_upd_data.first_name}, last_name: {before_upd_data.last_name}')
    
    userUpdate(10001, 'Misaka')
    
    after_upd_datas = getFilterUser(10001)
    for after_upd_data in after_upd_datas:
        print(f'After Update User ... user_id: {after_upd_data.user_id}, first_name: {after_upd_data.first_name}, last_name: {after_upd_data.last_name}')
    