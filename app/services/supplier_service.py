from app.models.supplier import Supplier #service va al repository
from app.repositories.supplier_repository import SupplierRepository
from app import cache

class SupplierService: #van las tareas
    def __init__(self): #__init__ es el inicializador de atributos
        self.__repo = SupplierRepository()
    
    def find_by_id(self, id) -> Supplier:
#        self.__repo = cache.get(id)
#        if self.__repo is None:
#            self.__repo = SupplierRepository.find_by_id(id)
#            cache.set(self.__repo.id, SupplierRepository, timeout=50) #si ya pasaron 50 seg lo va a buscar y lo guarda por 50 seg
        return self.__repo.find_by_id(id)
    
    def find_by_name(self, name) -> list:
        return self.__repo.find_by_name(name)
    
    def find_by_email(self, email) -> Supplier:
        return self.__repo.find_by_email(email)
    
    def find_all(self) -> Supplier:
        return self.__repo.find_all()
    
    def create(self, entity: Supplier) -> Supplier:
        #cache.set(self.__repo.id, self.__repo, timeout=50)
        return self.__repo.create(entity) #crea
    
    def update(self, dto, id:int) -> Supplier:
        return self.__repo.update(dto, id)
    
    def delete(self, id:int) -> Supplier:
        return self.__repo.delete(id)

    