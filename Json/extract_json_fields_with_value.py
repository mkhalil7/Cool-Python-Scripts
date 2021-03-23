import json

# json path
path = 'sampleJson.json'
outputFile = "output"
o = open(outputFile, "w")

# The purpose of the script is to extract the fields and their value from a json file

def iterate_multidimensional(my_dict, level=0):
    for k, v in my_dict.items():
        if (isinstance(v, dict)):
            print((' ' * 4) * level + k + ":")
            o.write((' ' * 4) * level + k + ":" + "\n")
            iterate_multidimensional(v, level + 1)
            continue
        print((' ' * 4) * level + k + " : " + str(v))
        o.write((' ' * 4) * level + k + " : " + str(v) + "\n")


# file needs to be placed in the same folder as the script with the name json_sample.json
f = open(path, "r")
requestJSON = json.load(f)
iterate_multidimensional(requestJSON)
