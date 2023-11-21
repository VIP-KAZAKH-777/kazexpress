from flask_restful import Api, Resource, reqparse
import models.crud
import json
from app import api

class Product(Resource):
    def get(self, pid):
        return models.crud.get_products(pid)
    
    def post(self, pid):
        parser = reqparse.RequestParser()
        parser.add_argument("sid", type=int, required=True)
        parser.add_argument("category", type=str, required=True)
        parser.add_argument("price", type=str, required=True)
        parser.add_argument("name", type=str, required=True)
        parser.add_argument("description", type=str, required=True)
        parser.add_argument("media", type=str, required=True)
        parser.add_argument("characs", type=str, required=True)
        parser.add_argument("reviews", type=str, required=True)
        parser.add_argument("demand", type=int, required=True)
        parser.add_argument("stars", type=int, required=True)

        abc = parser.parse_args()
        return models.crud.add_product(abc)
 
    def put(self, pid):
        parser = reqparse.RequestParser()
        parser.add_argument("pid", type=int, required=True)
        parser.add_argument("sid", type=int, required=True)
        parser.add_argument("category", type=str, required=True)
        parser.add_argument("price", type=str, required=True)
        parser.add_argument("name", type=str, required=True)
        parser.add_argument("description", type=str, required=True)
        parser.add_argument("media", type=str, required=True)
        parser.add_argument("characs", type=str, required=True)
        parser.add_argument("reviews", type=str, required=True)
        parser.add_argument("demand", type=int, required=True)
        parser.add_argument("stars", type=int, required=True)

        abc = parser.parse_args()
        return models.crud.update_product(abc)
    
    #No reason in realisation
    def delete(self, pid):
        pass

