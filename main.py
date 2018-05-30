import os
import sys
import argparse 

parser = argparse.ArgumentParser(usage=sys.argv[0]+" [-n] name [-c] counter")
parser.add_argument('-n', '--name', help="New name of the files")
parser.add_argument('-c', '-counter', help='Number from which program starts adding to name ')

args = parser.parse_args()

#comment

try:
  oldNames = os.listdir(sys.argv[1])

  if not os.listdir(sys.argv[1]):
    sys.exit(sys.argv[1]+" is empty")  
  
  newName = sys.argv[2] + "_"
  counter = int(sys.argv[3])
  path = sys.argv[1]
  fileCounter = 0

  for filename in oldNames:
    name, ext = os.path.splitext(path+'/'+filename)
    os.rename(path+'/'+filename, path+'/'+newName+str(counter)+ext)
    

    print("Renaming: "+filename+" to: "+newName+str(counter)+ext)

    fileCounter+=1
    counter+=1

  print(str(fileCounter)+" files renaming successfully done!")

except OSError:
  print("Cannot open "+sys.argv[1])

except IndexError:
  print("Incompleted argument list")




