import time
import uuid
from datetime import datetime
from decimal import Decimal

from json_util import dumps, loads

json_ = {"MyString": "a",
         "num": 4,
         "MyBool": False,
         "my_dict": {"my_date": datetime.utcnow()},
         "MyNone": None,
         "MyZero": 0,
         "myDecimal": Decimal("19.2"),  # converts Decimal to float, load it as float
         "myLong": long(1938475658493),
         "MyNestedDict": {
             "my_other_nested": {
                 "name": "John",
                 "surname": "Lennon",
                 "MyOtherNone": None,
                 "floaty": float(29.4),
                 "myList": [1, 3, 4, 5, 6, "This Is Sparta!"],
                 "mySet": {1, 3, 4, 5, 6},  # converts set to list, returns as list
                 "myUUID": uuid.uuid4(),  # converts uuid to string, loads it as string
                 "time": time.time()  # converts it to seconds python float, loads it as float
             }
         }
    }

dynamodb_json = dumps(json_)
print dynamodb_json
print loads(dynamodb_json)
