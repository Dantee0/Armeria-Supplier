import unittest
import subprocess
import time
import requests
from app import create_app, db, cache

class TestRequests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Inicia el servidor Flask en un proceso separado
        cls.server_process = subprocess.Popen(['flask', 'run', '--port', '5000'])
        # Espera un poco para asegurarse de que el servidor esté en ejecución
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        # Detén el servidor Flask
        cls.server_process.terminate()
        cls.server_process.wait()

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

    def test_create(self):
        body = {"name": "Bersa", "cuil": "29050602215", "email": "bersa@gmail.com", "code": "1922228"}
        response = requests.post('http://127.0.0.1:5000/api/v1/create', json=body)
        response_json = response.json()
        self.assertEqual(response_json["id"], 1)
        self.assertEqual(response_json["name"], 'Bersa')
        self.assertEqual(response_json["cuil"], '29050602215')
        self.assertEqual(response_json["code"], '1922228')
        self.assertEqual(response_json["email"], 'bersa@gmail.com')

if __name__ == '__main__':
    unittest.main()

'''import unittest
from sqlalchemy import text
import requests
from app.services.supplier_service import Supplier, SupplierService
from app import create_app, db , cache

service = SupplierService()


class TestRequests(unittest.TestCase):


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
        supplier.cuil = '29050602215'
        supplier.email = 'bersa@gmail.com'
        supplier.code = '1922228'
        supplier_db = service.create(supplier)
        return supplier_db


    def test_create(self):
        body = {"name": "Bersa", "cuil": "29050602215", "email": "bersa@gmail.com", "code": "1922228"}
        response = requests.post('http://127.0.0.1:5000/api/v1/supplier/create', json=body)
        response = response.json()
        self.assertEqual(response["id"], 1)
        self.assertEqual(response["name"], 'Bersa')
        self.assertEqual(response["cuil"], '29050602215')
        self.assertEqual(response["code"], '1922228')
        self.assertEqual(response["email"], 'bersa@gmail.com')


if __name__ == '__main__':
    unittest.main()'''