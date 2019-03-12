from xml.sax.handler import ContentHandler
from xml.sax import make_parser
from glob import glob
import sys

def parsefile(file):
    parser = make_parser()
    parser.setContentHandler(ContentHandler())
    parser.parse(file)

file_path = sys.argv[1]

try:
    parsefile(file_path)
    #print "Everything is ok!"
except Exception, e:
    print "Error:", e
