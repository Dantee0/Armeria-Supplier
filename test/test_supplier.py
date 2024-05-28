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

   
    def test_app(self):
        self.assertIsNotNone(current_app)


    def test_supplier(self):
        supplier = Supplier()
        supplier.email = 'test@example.com'
        self.assertEqual(supplier.email, 'test@example.com')


    def test_create_supplier(self):
        supplier = self.__createsupplier()
        self.assertGreaterEqual(supplier.id, 1)


    def __createsupplier(self):
        supplier = Supplier()
        supplier.name = 'Glock'
        supplier.cuil = '29050602'
        supplier.email = 'test@example.com'
        supplier.code = '1922228'
        SupplierService.create(supplier)
        return supplier
    

    def test_find_by_id(self):
        _ = self.__createsupplier()
        supplier = SupplierService.find_by_id(1)
        self.assertIsNotNone(supplier)
        self.assertIsNotNone(supplier.name, 'Glock')
        self.assertIsNotNone(supplier.cuil, '29050602')
        self.assertIsNotNone(supplier.email, 'test@example')
        self.assertIsNotNone(supplier.code, '1922228')

   
    def test_find_all(self):
        _ = self.__createsupplier()
        suppliers = SupplierService.find_all()
        self.assertGreaterEqual(len(suppliers), 1)

    
    def test_update(self):
        supplier = self.__createsupplier()
        supplier.name = 'Bersa'
        supplier.cuil = '22521187'
        supplier.email = 'bersa@example'
        supplier.code = '1455557'
        SupplierService.update(supplier, 1)
        result = SupplierService.find_by_id(1)
        self.assertEqual(result.name, supplier.name)
        self.assertEqual(result.cuil, supplier.cuil)
        self.assertEqual(result.email, supplier.email)
        self.assertEqual(result.code, supplier.code)

   
    def test_delete(self):
        _ = self.__createsupplier()
        SupplierService.delete(1)
        suppliers = SupplierService.find_all()
        self.assertEqual(len(suppliers), 0)


if __name__ == '__main__':
    unittest.main()