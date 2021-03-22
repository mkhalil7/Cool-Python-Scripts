import json

#place the jsonFile containing the Json in the same folder as this script and run

f= open("jsonFile.json" )
data = json.load(f)
print(json.dumps(data, indent=5))
