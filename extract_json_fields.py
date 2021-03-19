import json

#The purpose of the script is to extact the fields from 

def iterate_multidimensional(my_dict):
    for k,v in my_dict.items():
        if(isinstance(v,dict)):
            print(k+"")
            iterate_multidimensional(v)
            continue
        print(k)

# file needs to be paced in the same folder as the script woth the name json_sample.json
f = open('json_sample.json', 'r')
requestJSON = json.load(f)
iterate_multidimensional(requestJSON)
