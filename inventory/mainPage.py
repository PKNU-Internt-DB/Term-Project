
from .models import *
import json

def getMain1():
    warehouses_list=[]
    warehouse_ids=Warehouses.objects.values('warehouse_id')
    
    for ware_id in warehouse_ids:
        inven=Inventories.objects.filter(warehouse=ware_id['warehouse_id']).values('product','quantity')
                
        tmp_dict = dict()
        tmp_dict['ware_id'] = ware_id['warehouse_id']
        
        count = 0
        for i in inven:
            count += int(i['quantity'])

        tmp_dict['quantity'] = count            
        warehouses_list.append(tmp_dict)

    obj1 = json.dumps(warehouses_list, indent="\t")
    print(obj1)

    return obj1


# def getMain2(ware_id):
#     warehouses_dict={}
    
#     # warehouse_ids=Warehouses.objects.values('warehouse_id')
    
#     # print('디버그')
#     # print(warehouse_ids)
#     # for ware_id in warehouse_ids:
    
#     inven=Inventories.objects.filter(warehouse=ware_id).values('product','quantity')
    
#     warehouses_dict[ware_id['warehouse_id']]={}
#     for i in inven:

#             warehouses_dict[ware_id['warehouse_id']][i['product']]=int(i['quantity'])
#     obj1 = json.dumps(warehouses_dict, indent="\t")
    
#     print(obj1)

#     return obj1

def getMain3(ware_id):
    # print(ware_id)
    product=Inventories.objects.filter(warehouse=float(ware_id)).values('product','quantity')
    # print(list(product))
    obj1 = json.dumps(list(product))
    # print(obj1)

    return obj1
