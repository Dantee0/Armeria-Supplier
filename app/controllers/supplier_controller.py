from flask import Blueprint, jsonify, request
from app.services.supplier_service import SupplierService
from ..mapping.supplier_schema import SupplierSchema

service = SupplierService()
supplier_schema_many = SupplierSchema(many=True)
supplier_schema = SupplierSchema()
supplier = Blueprint('supplier', __name__)


@supplier.route('/supplier/', methods=['GET'])
def index():
    list = service.find_all()
    result = supplier_schema_many.dump(list)
    resp = jsonify(result)
    resp.status_code = 200
    return resp


@supplier.route('/supplier/id/<int:id>', methods=['GET'])
def find_by_id(id):
    response = supplier_schema.dump(service.find_by_id(id))
    resp = jsonify(response)
    resp.status_code = 200
    return resp


@supplier.route('/supplier/create/', methods=['POST'])
def create_supplier():
    supplier = supplier_schema.load(request.json)
    response = supplier_schema.dump(service.create(supplier))
    resp = jsonify(response)
    resp.status_code = 200
    return resp


@supplier.route('/supplier/name/', methods=['GET'])
def find_by_name():
    name = request.args.get('name')
    response = supplier_schema_many.dump(service.find_by_name(name))
    resp = jsonify(response)
    resp.status_code = 200
    return resp
    if response:
        response_builder.add_message("Nombre encontrado").add_status_code(100).add_data({'suppliers':response})


@supplier.route('/supplier/email/<string:email>', methods=['GET'])
def find_by_email(email):
    response = supplier_schema.dump(service.find_by_email(email))
    resp = jsonify(response)
    resp.status_code = 200
    return resp


@supplier.route('/supplier/update/<int:id>', methods=['PUT'])
def update_supplier(id):
    supplier = request.json
    response = supplier_schema.dump(service.update(supplier, id))
    resp = jsonify(response)
    resp.status_code = 200
    return resp


@supplier.route('/supplier/delete/<int:id>', methods=['DELETE'])
def delete_supplier(id):
    response = supplier_schema.dump(service.delete(id))
    resp = jsonify(response)
    resp.status_code = 200
    return resp

