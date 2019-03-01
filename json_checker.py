import sys
import json

def json_validation(data):
    try:
        json.loads(data)
        #print "Everything is ok!"
        return True
    except ValueError as e:
        print "Error: ", e
        return False

file_path = sys.argv[1]
file = open(file_path, 'r')
string = file.read()
# print string
json_validation(string)
