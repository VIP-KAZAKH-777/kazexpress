import json

def get_categories():
    f = open('models/product_categories.json')
    data = json.load(f)
    f.close()
    return data