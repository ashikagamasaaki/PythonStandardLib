from db.dbengine import User
from db.dbopen import SessionCreater
from abc import ABC, abstractmethod

# test_user = User(user_id='10004', first_name='Takashi', last_name='Goto', age=40)

# session = SessionCreater.makeSession()
# session.add(test_user)
# session.commit()
# session.close()

class DataRegister(ABC):
    def __init__(self):
        self.session = SessionCreater.makeSession()
    
    @abstractmethod
    def register(self, datas: dict):
        pass

class UserRegister(DataRegister):
    def register(self, datas: dict):
        # 登録データ取得
        rgt_user_id = datas.get('user_id')
        rgt_first_name = datas.get('first_name')
        rgt_last_name = datas.get('last_name')
        rgt_age = datas.get('age')
        
        # ユーザデータ登録処理
        user_data = User(user_id=rgt_user_id, first_name=rgt_first_name, last_name=rgt_last_name, age=rgt_age)
        self.session.add(user_data)
        self.session.commit()
        self.session.close()



if __name__ == '__main__':
    user_data = {'user_id':10005, 'first_name': 'Rintaro', 'last_name': 'Tsumugi', 'age': 16}
    user_register = UserRegister()
    user_register.register(user_data)
