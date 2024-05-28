from app.config.database import db
from sqlalchemy.ext.hybrid import hybrid_property
from dataclasses import dataclass

# @dataclass
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
    
    def __init__(self, name:str, cuil:str, email:str, code:str): #Constructor(parametros)
        self.__name = name
        self.__cuil = cuil
        self.__email = email
        self.__code = code

    @hybrid_property #lo encapsula en un atributo, el get lo pide para leer
    def id(self)->int:
        return self.__id
    
    @id.setter # es cuando se crea el objeto
    def id(self, id:int):
        self.__id = id

    @hybrid_property #seria como get name, agrega funcionalidad mas a un metodo
    def code(self)-> str: #ver si es int o str
        return self.__code
    
    @code.setter #seria como set name, el arroba es un decorador, un patron de diseño
    def code (self, code:str):
        self.__code = code
    
    
    @hybrid_property
    def name(self)->str:
        return self.__name
    
    @name.setter #le pasamos el valor del atributo al que esta en la clase
    def name (self, name:str):
        self.__name = name


    @hybrid_property
    def cuil(self)->str:
        return self.__cuil
    
    @cuil.setter
    def cuil (self, cuil:str):
        self.__cuil = cuil

    
    @hybrid_property
    def email(self)->str:
        return self.__email
    
    @email.setter
    def email (self, email:str):
        self.__email = email


    def __repr__(self) -> str: #  da la informacion de cada objeto
        return f'Supplier: \n Nombre:{self.name}, \n Cuil:{self.cuil}, \n Email:{self.email}, \n Codigo:{self.code}'
    
    def __eq__(self,__value:object) -> bool: #comparamos si dos objetos son iguales, para no agregar dos veces el mismo objeto
        return self.codigo == __value.code and self.name == __value.name
    