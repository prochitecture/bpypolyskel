import argparse, os
from mathutils import Vector
from urllib import request

#
# Command line arguments
#
argParser=argparse.ArgumentParser()
argParser.add_argument("--log", help="Path to a log file with OSM ids", required=True)
argParser.add_argument("--outputDir", help="Folder for the downloaded OSM files", required=True)
args=argParser.parse_args()
logFilepath = args.log
outputDir = args.outputDir


with open(logFilepath, 'r') as logFile:
    while True:
        line = logFile.readline()
        if not line:
            break
        problem = line[:line.find(':')]
        if problem in ("Flat roof", "Not hipped roof"):
            continue
        osmId = line[line.rfind(':')+1:-1]
        print(osmId)
        request.urlretrieve(
            "http://overpass-api.de/api/interpreter",
            os.path.join(outputDir, "%s_.osm" % osmId),
            None,
            ("((way(%s););node(w););out;" % osmId).encode('ascii')
        )