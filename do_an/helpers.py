import json
import os
import pathlib

current_directory = os.getcwd()
contents = str(pathlib.Path(__file__).parent.absolute())
def get_users_from_file():
    data = []
    url = contents+'\data.json'
    if os.path.exists(url):
        f = open(url ,encoding='utf-8')
        result = json.load(f)
        if "users" in result:
            data = result["users"]
           
    else:
        f = open(url, "w")
        with open(url, "w", encoding='utf8') as outfile:
            outfile.write("[]")
    return data

def dumper(obj):
    try:
        return obj.toJSON()
    except:
        return obj.__dict__

def set_data_to_file(users):
    obj = dict({"users": users})
    json_object = json.dumps(obj, ensure_ascii=False)
 
    with open(contents+'\data.json', "w", encoding='utf8') as outfile:
        outfile.write(json_object)
    

