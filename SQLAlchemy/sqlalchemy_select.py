from db.dbengine import User, Assign, Department, Employee
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


def getEmpDept(isouter_flg=False):
    session = getSession()
    user_dept = session.query(Employee, Employee.emp_id, Employee.emp_name, Department.dept_id, Department.dept_name).\
        join(Assign, Employee.emp_id == Assign.emp_id, isouter=isouter_flg).\
        join(Department, Assign.dept_id == Department.dept_id, isouter=isouter_flg).\
        all()
    session.close()
    return user_dept




if __name__ == '__main__':
    # users = getAllUser()
    # for user in users:
    #     print(f'User ... user_id: {user.user_id}, first_name: {user.first_name}, last_name: {user.last_name}')
    
    
    # filter_users = getFilterUser(10003)
    # for filter_user in filter_users:
    #     print(f'Filter User ... user_id: {filter_user.user_id}, first_name: {filter_user.first_name}, last_name: {filter_user.last_name}')    
    
    
    # emp_dept_datas = getEmpDept()
    # for emp_dept_data in emp_dept_datas:
        # print(f'Emp: {emp_dept_data.emp_name}({emp_dept_data.emp_id}), Dept: {emp_dept_data.dept_id}({emp_dept_data.dept_name})')
    
    
    all_emp_dept_datas = getEmpDept(isouter_flg=True)
    for emp_dept_data in all_emp_dept_datas:
        print(f'Emp: {emp_dept_data.emp_name}({emp_dept_data.emp_id}), Dept: {emp_dept_data.dept_id}({emp_dept_data.dept_name})')