from app.models import Supplier 
from app.config.database import db
from .CRUD import Create, Read, Update, Delete


class SupplierRepository(Read, Update, Create, Delete):

    def __init__(self):
        self.__model = Supplier
    
    """
    Hacemos una busqueda y nos trae todos los proveedores
    """
    def find_all(self): 
        return db.session.query(self.__model).all()
    
    """
    Hacemos una busqueda por id del proveedor
    """
    def find_by_id(self, id: int) -> Supplier: #Read
        return db.session.query(self.__model).filter(self.__model.id == id).one()
    
    """
    Recibe el proveedor creado y lo guarda en la base de datos
    """
    def create(self, supplier: Supplier): 
        db.session.add(supplier)
        db.session.commit()
        return supplier
    
    """
    Hacemos una busqueda por nombre de proveedor
    """
    def find_by_name(self, name: str) -> list:
        list = db.session.query(self.__model).filter(self.__model.name.like(name)).all() 
        return list
    
    """
    Borramos el proveedor por su id
    """
    def delete(self, id: int):
        entity = self.find_by_id(id) 
        db.session.delete(entity)
        db.session.commit()
        return entity
    
    """
    Hacemos una busqueda por emali de proveedor
    """
    def find_by_email(self, email: str) -> Supplier:
        return db.session.query(self.__model).filter(self.__model.email == email).first() 
    
    """
    Podemos modificar los atributos del proveedor segun el id
    """
    def update(self,dto, id: int) -> Supplier: # data transfer object(dto)
        entity = self.find_by_id(id)
        for key, value in dto.items():
            setattr(entity, key, value)
        db.session.commit()
        return entity