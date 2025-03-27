from __future__ import annotations
from app import db
from sqlalchemy.ext.hybrid import hybrid_property
from dataclasses import dataclass


@dataclass
class Supplier(db.Model):
    __tablename__ ='supplier'
    id = db.Column('id' , db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('name' , db.String(250))
    cuil= db.Column('cuil', db.String(250))
    email= db.Column('email', db.String(250))
    code= db.Column('code', db.String(250)) 


    """
    name: str name of supplier max char 250
    cuil: str cuil of supplier max char 250
    email: str email of supplier max char 250
    code: str code of supplier max char 250
    """

