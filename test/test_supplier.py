import unittest
from app import create_app, db
from app.models import Supplier
from flask import current_app
from app.services import SupplierService

service = SupplierService()

class TestSupplier(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    
    def tearDown(self) -> None: #por cada uno de los test se ejecuta
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    
    def test_create_supplier(self):
        supplier = self.__create_supplier()
        self.assertGreaterEqual(supplier.id, 1)

   
    def __create_supplier(self):
        supplier = Supplier('Glock','29050602','test@example.com','1922228')
        service.create(supplier)
        return supplier
    

    def test_find_by_id(self):
        supplier = self.__create_supplier()
        service.find_by_id(1)
        self.assertEqual(supplier.name, 'Glock')
        self.assertEqual(supplier.cuil, '29050602')
        self.assertEqual(supplier.email, 'test@example.com')
        self.assertEqual(supplier.code, '1922228')


    def test_find_all(self):
        _ = self.__create_supplier()
        suppliers = service.find_all()
        self.assertGreaterEqual(len(suppliers), 1)


    def test_update(self):
        supplier = self.__create_supplier()
        supplier.name = 'Bersa'
        supplier.cuil = '22521187'
        supplier.email = 'bersa@example'
        supplier.code = '1455557'
        result = service.find_by_id(1)
        self.assertEqual(result.name,'Bersa')
        self.assertEqual(result.cuil,'22521187')
        self.assertEqual(result.email,'bersa@example')
        self.assertEqual(result.code,'1455557')


    def test_delete(self):
        _ = self.__create_supplier()
        service.delete(1)
        suppliers = service.find_all()
        self.assertEqual(len(suppliers), 0)


if __name__ == '__main__':
    unittest.main()