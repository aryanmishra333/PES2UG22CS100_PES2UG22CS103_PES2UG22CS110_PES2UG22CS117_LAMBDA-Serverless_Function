from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from .database import Base , engine 

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)

    # Relationship to connect User to their Functions
    functions = relationship("Function", back_populates="owner", cascade="all, delete-orphan")


class Function(Base):
    __tablename__ = "function"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False)
    description = Column(Text)
    created_at = Column(TIMESTAMP, nullable=False)
    route = Column(String(255), unique=True, nullable=False)
    code = Column(Text, nullable=False)
    runtime = Column(String(50), nullable=False)  # Matches the database constraint
    timeout = Column(Integer, default=5000)
    memory = Column(Integer, default=128)
    is_active = Column(Boolean, default=True)
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"))

    # Relationship to connect Function to its Owner (User)
    owner = relationship("User", back_populates="functions")