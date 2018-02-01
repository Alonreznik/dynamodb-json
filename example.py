from __future__ import print_function

import time
import uuid
from datetime import datetime
from decimal import Decimal

from dynamodb_json import json_util as json

json_ = {"MyString": "a",
         "num": 4,
         "MyBool": False,
         "my_dict": {"my_date": datetime.utcnow()},
         "MyNone": None,
         "MyZero": 0,
         "myDecimal": Decimal("19.2"),  # converts Decimal to float, load it as float
         "myLong": int(1938475658493),
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

as_dict = False
dynamodb_json = json.dumps(json_, as_dict=True)
print(dynamodb_json)
# {
# "my_dict": {"M": {"my_date": {"S": "2017-04-22T14:41:35.780000"}}},
# "MyBool": {"BOOL": false}, "MyNone": {"NULL": true},
# "MyNestedDict": {
#   "M": {"my_other_nested": {
#       "M": {"myUUID": {"S": "2f4ad21e098f49b18e22ad209779048b"},
#             "surname": {"S": "Lennon"}, "name": {"S": "John"},
#             "mySet": {"L": [{"N": "1"}, {"N": "3"}, {"N": "4"}, {"N": "5"}, {"N": "6"}]},
#             "floaty": {"N": "29.4"}, "time": {"N": "1492872095.78"},
#             "myList": {"L": [{"N": "1"}, {"N": "3"}, {"N": "4"}, {"N": "5"}, {"N": "6"}, {"S": "This Is Sparta!"}]},
#             "MyOtherNone": {"NULL": true}}
#             }
#       }
#   },
# "myDecimal": {"N": "19.2"}, "num": {"N": "4"},
# "MyString": {"S": "a"},
# "myLong": {"N": "1938475658493"},
# "MyZero": {"N": "0"}
# }

my_dict = json.loads(dynamodb_json)
print(my_dict)

# {'my_dict': {'my_date': datetime.datetime(2017, 4, 22, 14, 41, 35, 780000)}, 'MyBool': False, 'MyNone': None,
#  'MyNestedDict': {
#      'my_other_nested': {'myUUID': '2f4ad21e098f49b18e22ad209779048b',
#                          'surname': 'Lennon', 'name': 'John',
#                          'mySet': [1, 3, 4, 5, 6],
#                          'floaty': 29.4,
#                          'time': 1492872095.78,
#                          'myList': [1, 3, 4, 5, 6, 'This Is Sparta!'],
#                          'MyOtherNone': None
#                          }
#              },
#  'myDecimal': 19.2,
#  'num': 4,
#  'MyString': 'a',
#  'myLong': 1938475658493L,
#  'MyZero': 0
# }
