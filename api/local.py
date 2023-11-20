import requests

res2 = requests.post("http://127.0.0.1:5000/api/product/1", json={
            "sid":"1",
            "category":"mobile_phones",
            "price":"520.000kzt",
            "name":"iPhone 2210 Super",
            "description":"RAM. There is 6GB RAM in the iPhone 15 and 15 Plus, the same amount of RAM that was in the iPhone 14 models. Storage Space. Storage space starts at 128GB for the most affordable versions of the iPhone 15 and 15 Plus, but 256GB and 512GB options are available at increased prices. USB-C Port. The iPhone 15 models are the first to feature a USB-C port instead of a Lightning port, allowing them to be charged with a USB-C cable.",
            "media":1,
            "characs":{
                "origin": "country",
                "brand name": "No/brand",
                "category": "category",
                "deliver": "free/cost",
                "bought": "999",
                "use": "purpose"
            },
            "reviews":{
                "author": {
                        "name": "user name",
                        "avatar": "avatar",
                        "location": "delivered location"
                },
                "description": "review text",
                "date": "created time",
                "stars": "4.5"
            },
            "demand":300,
            "stars":3
        })

print(res2)