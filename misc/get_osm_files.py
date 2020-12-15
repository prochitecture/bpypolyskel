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
        # Position of the separator between the type of the OSM elemement (way or relation) and
        # the status string
        statusPosition = line.rfind('|')
        status = line[statusPosition+1:-1]
        if status in ("Flat roof", "Not hipped roof"):
            continue
        # position of the separator between the osm id and the type of the OSM element (way or relation)
        elementTypePosition = line.find('|')
        osmId = line[:elementTypePosition]
        osmType = line[elementTypePosition+1 : statusPosition]
        print(">%s< >%s< >%s<" % (osmId, osmType, status))
        request.urlretrieve(
            "http://overpass-api.de/api/interpreter",
            os.path.join(outputDir, "%s_.osm" % osmId),
            None,
            ("((way(%s););node(w););out;" % osmId).encode('ascii')\
                if osmType == "way" else\
                ("((relation(%s););way(r);node(w););out;" % osmId).encode('ascii')
            )