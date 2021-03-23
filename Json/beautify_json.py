import json

path = "sampleJson.json"
outputFile = "output"
# place the jsonFile containing the Json in the same folder as this script and run

f = open(path, "r")
o = open(outputFile , "w")
data = json.load(f)
print(json.dumps(data, indent=5))

o.write(json.dumps(data, indent=5))

