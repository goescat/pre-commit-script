import sys
import json

def json_validation(data):
    try:
        json.loads(data)
        print "True"
    except ValueError as e:
        print "Error: ", e

file_path = sys.argv[1]
file = open(file_path, 'r')
string = file.read()
# print string
json_validation(string)
