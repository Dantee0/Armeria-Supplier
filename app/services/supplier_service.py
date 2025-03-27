from app.models import Supplier #service va al repository
from app.repositories.supplier_repository import SupplierRepository
from app import cache
from tenacity import retry, stop_after_attempt, stop_after_delay


class SupplierService: #van las tareas
    def __init__(self): #__init__ es el inicializador de atributos
        self.__repo = SupplierRepository()
    

    def find_by_id(self, id: int) -> Supplier:
        supplier = cache.get(str(id))
        if supplier == None:
            supplier = self.__repo.find_by_id(id)
            cache.set(str(supplier.id), supplier, timeout=50) #lo guarda por 50 seg
        return supplier
    

    @retry(stop=(stop_after_delay(10) | stop_after_attempt(5)))
    def find_by_name(self, name) -> list:
        supplier = cache.get(str(name))
        if supplier == None:
            supplier = self.__repo.find_by_name(name)
            print(supplier)
            supplier = supplier[0]
            cache.set(str(supplier.name), supplier, timeout=50)
        return supplier
    

    @retry(stop=(stop_after_delay(10) | stop_after_attempt(5)))
    def find_by_email(self, email) -> Supplier:
        supplier = cache.get(str(email))
        if supplier == None:
            supplier = self.__repo.find_by_email(email)
            cache.set(str(supplier.email), supplier, timeout=50)
        return supplier
    

    @retry(stop=(stop_after_delay(10) | stop_after_attempt(5)))
    def find_all(self) -> Supplier:
        return self.__repo.find_all()
    

    @retry(stop=(stop_after_delay(10) | stop_after_attempt(5)))
    def create(self, entity: Supplier) -> Supplier:
        supplier = self.__repo.create(entity)
        cache.set(str(supplier.id), supplier, timeout=50)
        return supplier
    

    @retry(stop=(stop_after_delay(10) | stop_after_attempt(5)))
    def update(self, dto, id:int) -> Supplier:
        supplier = self.__repo.update(dto, id)
        cache.set(str(supplier.id), supplier, timeout=50)
        return supplier
    

    @retry(stop=(stop_after_delay(10) | stop_after_attempt(5)))
    def delete(self, id:int) -> Supplier:
        supplier = self.__repo.delete(id)
        cache.set(str(id), supplier, timeout=0)

    