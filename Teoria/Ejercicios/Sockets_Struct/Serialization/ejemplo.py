import json

data = {
    "word": "cafe"
}

# Serializar a JSON
json_string = json.dumps(data)
serialized_json = json_string.encode()
print(serialized_json)

print(len(serialized_json))

import pickle

pickled_data = pickle.dumps(data)
print(pickled_data)
print(len(pickled_data))