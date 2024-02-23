from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    age = Column(Integer)

class Employee(Base):
    __tablename__ = 'emp'
    emp_id = Column(Integer, primary_key=True)
    emp_name = Column(String(255))

class Department(Base):
    __tablename__ = 'dept'
    dept_id = Column(Integer, primary_key=True)
    dept_name = Column(String(255))

class Assign(Base):
    __tablename__ = 'assign'
    assign_id = Column(Integer, primary_key=True, autoincrement=True)
    emp_id = Column(Integer, ForeignKey("emp.emp_id", name="fk_test_assign_00"), nullable=False)
    dept_id = Column(Integer, ForeignKey("dept.dept_id", name="fk_test_assign_01"), nullable=False)
    emp=relationship('Employee')
    dept=relationship('Department')


if __name__ == '__main__':
    engine = create_engine("mysql://root:root@localhost:3306/testdb")
    Base.metadata.create_all(bind=engine)