from .models import *
import json
def getProduct():
    product=Products.objects.values('product_name','list_price','category','description')
    obj1=json.dumps(list(product))
    return obj1