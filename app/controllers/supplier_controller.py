from flask import Blueprint, jsonify, request
from app.services.supplier_service import SupplierService
from ..mapping.supplier_schema import SupplierSchema

service = SupplierService()
supplier_schema_many = SupplierSchema(many=True)
supplier_schema = SupplierSchema()
supplier = Blueprint('supplier', __name__)


@supplier.route('/all/', methods=['GET'])#
def index():
    list = service.find_all()
    result = supplier_schema_many.dump(list)
    resp = jsonify(result)
    resp.status_code = 200
    return resp


@supplier.route('/id/<int:id>', methods=['GET'])
def find_by_id(id):
    response = supplier_schema.dump(service.find_by_id(id))
    resp = jsonify(response)
    resp.status_code = 200
    return resp


@supplier.route('/create/', methods=['POST'])#
def create_supplier():
    supplier = supplier_schema.load(request.json)
    response = supplier_schema.dump(service.create(supplier))
    resp = jsonify(response)
    resp.status_code = 200
    return resp


@supplier.route('/email/<string:email>', methods=['GET'])#
def find_by_email(email):
    response = supplier_schema.dump(service.find_by_email(email))
    resp = jsonify(response)
    resp.status_code = 200
    return resp


@supplier.route('/update/<int:id>', methods=['PUT'])#
def update_supplier(id):
    supplier = request.json
    response = supplier_schema.dump(service.update(supplier, id))
    resp = jsonify(response)
    resp.status_code = 200
    return resp


@supplier.route('/delete/<int:id>', methods=['DELETE'])#
def delete_supplier(id):
    response = supplier_schema.dump(service.delete(id))
    resp = jsonify(response)
    resp.status_code = 200
    return resp

