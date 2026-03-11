import request 
import json

URL = ""

data = {
    'name' : 'Abuzar Ali',
    'roll' : 4578,
    'city' : 'lahore'
}



json_data = json.dumps(data)

r = request.post(url = URL , data = json_data)



data = r.json()

print(data)