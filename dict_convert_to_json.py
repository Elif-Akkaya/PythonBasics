#to create json output we need to import json
import json
#first create a dict

my_dict = {"name" : "Elif", "surname" : "Akkaya", "no": 123}

#let's see if its type is dict or not

print(type(my_dict))

#it is ok, then continue to json

data_json = json.dumps(my_dict)
print(data_json)