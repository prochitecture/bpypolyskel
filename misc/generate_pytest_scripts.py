import os, sys, json
import bpy


blosmPath = None
osmFilesDir = None
outputDir = None
assetsDir = None
outputTemplate = None
outputFileNamePrefix = None

# read the values for the above variables from the config JSON file
with open(os.path.join(os.path.abspath(os.getcwd()), "config_generate_pytest_scripts.txt"), 'r') as configJsonFile:
    globals().update( json.load(configJsonFile) )
bpy.context.scene["outputDir"] = outputDir
bpy.context.scene["outputTemplate"] = outputTemplate
bpy.context.scene["outputFileNamePrefix"] = outputFileNamePrefix

print(blosmPath, osmFilesDir, outputDir)


sys.path.insert(0,  os.path.join(blosmPath, os.pardir))
blosmModule = __import__("blender-osm")
blosmModule.register()
print(blosmModule)
blosm = bpy.context.scene.blosm
blosm.osmSource = 'file'
blosm.assetsDir = assetsDir
blosm.setupScript = os.path.join(blosmPath, "setup", "test_hipped.py")


for fileName in os.listdir(osmFilesDir):
    print(fileName)
    blosm.osmFilepath = os.path.join(osmFilesDir, fileName)
    bpy.ops.blosm.import_data()
