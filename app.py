import os

inputFolder = "input"
outputFolder = "output"
included_extensions = ['jpg','jpeg', 'bmp', 'png', 'gif']

directory = f"{os.getcwd()}\{inputFolder}" #get directory path to input folder
file_names = [fn for fn in os.listdir(directory)if any(fn.endswith(ext) for ext in included_extensions)] # get list of allowed image files from input folder
print(file_names)

isExist = os.path.exists(outputFolder)
if not isExist:
    os.makedirs(outputFolder)

if not file_names:
    print("WARNING: No valid imagefile was found")
    input("Press enter to exit;")
else:
    for i in file_names:
        cmd = 'cwebp "'+inputFolder+'/'+i+'" -o '+outputFolder+'/'+i+'.webp"'
        os.system(cmd)