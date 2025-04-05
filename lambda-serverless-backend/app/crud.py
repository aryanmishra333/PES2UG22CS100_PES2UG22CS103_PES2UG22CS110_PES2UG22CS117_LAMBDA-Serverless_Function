from sqlalchemy.orm import Session
from .models import User, Function
from .schemas import UserCreate, FunctionCreate

# CRUD for User
def create_user(db: Session, user: UserCreate):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()

def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user

# CRUD for Function
def create_function(db: Session, function: FunctionCreate):
    db_function = Function(**function.dict())
    db.add(db_function)
    db.commit()
    db.refresh(db_function)
    return db_function

def get_functions(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Function).offset(skip).limit(limit).all()

def get_function(db: Session, function_id: int):
    return db.query(Function).filter(Function.id == function_id).first()

def update_function(db: Session, function_id: int, function: FunctionCreate):
    db_function = db.query(Function).filter(Function.id == function_id).first()
    if db_function:
        for key, value in function.dict().items():
            setattr(db_function, key, value)
        db.commit()
        db.refresh(db_function)
        return db_function
    return None

def delete_function(db: Session, function_id: int):
    db_function = db.query(Function).filter(Function.id == function_id).first()
    if db_function:
        db.delete(db_function)
        db.commit()
    return db_function