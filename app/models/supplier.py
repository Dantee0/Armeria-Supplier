from __future__ import annotations
from app import db
from sqlalchemy.ext.hybrid import hybrid_property
from dataclasses import dataclass


@dataclass
class Supplier(db.Model):
    __tablename__ ='supplier'
    __id = db.Column('id' , db.Integer, primary_key=True, autoincrement=True)
    __name = db.Column('name' , db.String(250))
    __cuil= db.Column('cuil', db.String(250), unique=True)
    __email= db.Column('email', db.String(250), unique=True)
    __code= db.Column('code', db.String(250), unique=True) 


    """
    name: str name of supplier max char 250
    cuil: str cuil of supplier max char 250
    email: str email of supplier max char 250
    code: str code of supplier max char 250
    """

