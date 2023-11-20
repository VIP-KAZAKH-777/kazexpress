from flask_restful import Api, Resource, reqparse
import models.crud
import json
from app import api

#json objects for product
def open_products_media(pid):
    return json.load(open('/uploads/products/media.json'))[pid]

class Product(Resource):
    def get(self, pid):
        return models.crud.get_products()
    
    def post(self, pid):
        parser = reqparse.RequestParser()
        parser.add_argument("sid", type=int)
        parser.add_argument("category", type=str)
        parser.add_argument("price", type=str)
        parser.add_argument("name", type=str)
        parser.add_argument("description", type=str)
        parser.add_argument("media", type=str)
        parser.add_argument("characs", type=str)
        parser.add_argument("reviews", type=str)
        parser.add_argument("demand", type=int)
        parser.add_argument("stars", type=int)

        abc = parser.parse_args()
        return models.crud.add_product(abc)
    
    def delete(self):
        return {}
    
    def put(self):
        return {}
    

