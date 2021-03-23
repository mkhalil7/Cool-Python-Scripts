import json

path = "sampleJson.json"
# place the jsonFile containing the Json in the same folder as this script and run

f = open(path, )

data = json.load(f)
print(json.dumps(data, indent=5))
