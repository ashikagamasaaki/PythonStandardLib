from db.dbengine import User, Employee, Department, Assign
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


class EmployeeRegister(DataRegister):
    def register(self, datas: dict):
        # 登録データ取得
        rgt_emp_id = datas.get('emp_id')
        rgt_emp_name = datas.get('emp_name')
        
        # 従業員データ登録処理
        emp_data = Employee(emp_id=rgt_emp_id, emp_name=rgt_emp_name)
        self.session.add(emp_data)
        self.session.commit()
        self.session.close()


class DepartmentRegister(DataRegister):
    def register(self, datas: dict):
        
        for data in datas:
            # 登録データ取得
            rgt_dept_id = data.get('dept_id')
            rgt_dept_name = data.get('dept_name')
            
            # 部署データ登録処理
            dept_data = Department(dept_id=rgt_dept_id, dept_name=rgt_dept_name)
            self.session.add(dept_data)
            self.session.commit()
        
        self.session.close()


class AssignRegister(DataRegister):
    def register(self, datas: dict):
        
        for data in datas:
            # 登録データ取得
            rgt_assign_id = data.get('assign_id')
            rgt_emp_id = data.get('emp_id')
            rgt_dept_id = data.get('dept_id')
            
            # 配属データ登録処理
            assign_data = Assign(assign_id=rgt_assign_id, emp_id=rgt_emp_id, dept_id=rgt_dept_id)
            self.session.add(assign_data)
            self.session.commit()
        
        self.session.close()


if __name__ == '__main__':
    # user_data = {'user_id':10005, 'first_name': 'Rintaro', 'last_name': 'Tsumugi', 'age': 16}
    # user_register = UserRegister()
    # user_register.register(user_data)
    
    # emp_data = {'emp_id':10004, 'emp_name': 'Tanaka Ichiro'}
    # emp_register = EmployeeRegister()
    # emp_register.register(emp_data)


    # dept_datas = [
    #         {'dept_id': 10001, 'dept_name': '総務部'},
    #         {'dept_id': 10002, 'dept_name': '人事部'},
    #         {'dept_id': 10003, 'dept_name': '経理部'},
    #         {'dept_id': 10004, 'dept_name': '情報システム部'}
    #     ]
    
    # dept_register = DepartmentRegister()
    # dept_register.register(dept_datas)


    
    assign_datas = [
            {'assign_id': 10001, 'emp_id': 10001, 'dept_id': 10001},
            {'assign_id': 10002, 'emp_id': 10002, 'dept_id': 10001},
            {'assign_id': 10003, 'emp_id': 10002, 'dept_id': 10002}
        ]
    
    assign_register = AssignRegister()
    assign_register.register(assign_datas)