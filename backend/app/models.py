
from sqlalchemy import Column,Integer,String,Float
from app.core.database import Base

class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True)
    email=Column(String)
    password_hash=Column(String)

class Santri(Base):
    __tablename__="santri"
    id=Column(Integer,primary_key=True)
    nama=Column(String)
    kelas=Column(String)

class Hafalan(Base):
    __tablename__="hafalan"
    id=Column(Integer,primary_key=True)
    santri_id=Column(Integer)
    nilai=Column(Float)
