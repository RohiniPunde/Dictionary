import json
from difflib import get_close_matches

data=json.load(open("data.json"))

def translate(w):
    w= w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys()))>0:
        yn=input("Did you match %s if Yes then print Y if No then N" %get_close_matches(w,data.keys())[0])
        if yn =='Y':
            return data[get_close_matches(w,data.keys())[0]]
        elif yn =='N':
            return "The data is not match"
        else:
            return "Query is not match"
    else:
        return "The data does not exist"


word=input("Enter word:")
output=translate(word)

if type(output)== list:
    for item in output :
        print(item)
else:
    print(output)