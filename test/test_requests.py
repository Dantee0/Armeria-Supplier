import unittest
from sqlalchemy import text
import requests
from app.services.supplier_service import Supplier, SupplierService
from app import create_app, db , cache

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
        body = {"name": "Bersa", "cuil": "29050602", "email": "test@gmail.com", "code": "1922228"}
        response = requests.post('http://127.0.0.1:5000/api/v1/supplier/create', json=body)
        response = response.json()
        self.assertGreaterEqual(response["id"], 1)
        self.assertEqual(response["name"], 'Bersa')
        self.assertEqual(response["cuil"], '29050602')
        self.assertEqual(response["email"], 'test@gmail.com')
        self.assertEqual(response["code"], '1922228')


    def test_find_by_id(self):
        supplier_db = self.create_supplier()
        supplier = self.app.test_supplier(use_cookies=True)
        response = supplier.get('http://localhost:5000/api/v1/supplier/id/1')
        response = response.get_json()
        self.assertEqual(response["id"], 1)


    def test_find_by_name(self):
        supplier_db = self.create_supplier()
        response = requests.get('http://127.0.0.1:5000/api/v1/supplier/name/', params={"name": "Bersa"})
        response = response.json()
        self.assertEqual(response["id"], 1)

    def test_find_by_email(self):
        supplier_db = self.create_supplier()
        supplier = self.app.test_supplier(use_cookies=True)
        response = supplier.get('http://127.0.0.1:5000/api/v1/supplier/email/test@gmail.com')
        response = response.get_json()
        self.assertEqual(response["id"], 1)

    
    def test_update(self) -> Supplier:
        supplier_db = self.create_supplier()
        supplier = self.app.test_supplier(use_cookies=True)
        body = {"name": "Glock", "cuil":"29151612", "email":"bersa@gmail.com", "code":"2911118"}
        response = supplier.put('http://localhost:5000/api/v1/client/update/1', json=body)
        response = response.get_json()
        self.assertEqual(response["id"], 1)
        self.assertEqual(response["name"], 'Glock')
        self.assertEqual(response["cuil"], '29151612')
        self.assertEqual(response["email"], 'bersa@gmail.com')
        self.assertEqual(response["code"], '2911118')
 

    def test_delete(self):
        supplier_db = self.create_supplier()
        supplier = self.app.test_supplier(use_cookies=True)
        response = supplier.delete('http://localhost:5000/api/v1/supplier/delete/1')
        suppliers = service.find_all()
        self.assertEqual(len(suppliers), 0)


if __name__ == '__main__':
    unittest.main()