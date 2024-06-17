import unittest
from flask import current_app
from app import create_app, db, cache
from app.services.supplier_service import Supplier, SupplierService

service = SupplierService()

class TestClient(unittest.TestCase):


    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()


    def tearDown(self):
        db.session.remove()
        db.drop_all()
        cache.clear()
        self.app_context.pop()


    def create_supplier(self):
        supplier = Supplier()
        supplier.name = 'Bersa'
        supplier.cuil = '29050602'
        supplier.email = 'test@gmail.com'
        supplier.code = '1922228'
        supplier_db = service.create(supplier)
        return supplier_db


    def test_create(self):
        supplier_db = self.create_supplier()
        self.assertGreaterEqual(supplier_db.id, 1)
        self.assertEqual(supplier_db.name, 'Bersa')
        self.assertEqual(supplier_db.cuil, '29050602')
        self.assertEqual(supplier_db.email, 'test@gmail.com')
        self.assertEqual(supplier_db.code, '1922228')


    def test_find_by_id(self):
        supplier_db = self.create_supplier()
        supplier = service.find_by_id(1)
        self.assertEqual(supplier.id, 1)
        self.assertEqual(supplier.name, 'Bersa')
        self.assertEqual(supplier.cuil, '29050602')
        self.assertEqual(supplier.email, 'test@gmail.com')
        self.assertEqual(supplier.code, '1922228')
        

    def test_find_by_name(self) -> list:
        supplier_db = self.create_supplier()
        supplier = service.find_by_name('Bersa')
        self.assertEqual(supplier.id, 1)
        self.assertEqual(supplier.name, 'Bersa')
        self.assertEqual(supplier.cuil, '29050602')
        self.assertEqual(supplier.email, 'test@gmail.com')
        self.assertEqual(supplier.code, '1922228')
    

    def test_find_by_email(self) -> Supplier:
        supplier_db = self.create_supplier()
        supplier = service.find_by_email('test@gmail.com')
        self.assertEqual(supplier.id, 1)
        self.assertEqual(supplier.name, 'Bersa')
        self.assertEqual(supplier.cuil, '29050602')
        self.assertEqual(supplier.email, 'test@gmail.com')
        self.assertEqual(supplier.code, '1922228')

    
    def test_update(self) -> Supplier:
        supplier_db = self.create_supplier()
        dto = {"name": "Glock", "cuil":"29151612", "email":"bersa@gmail.com", "code":"2911118"}
        supplier = service.update(dto, 1)
        result = service.find_by_id(1)
        self.assertEqual(result.id, 1)
        self.assertEqual(result.name, 'Glock')
        self.assertEqual(result.cuil, '29151612')
        self.assertEqual(result.email, 'bersa@gmail.com')
        self.assertEqual(result.code, '2911118')
 

    def test_delete(self) -> Supplier:
        supplier_db = self.create_supplier()
        service.delete(1)
        suppliers = service.find_all()
        self.assertEqual(len(suppliers), 0)



if __name__ == '__main__':
    unittest.main()