import os
import sys
import argparse 

parser = argparse.ArgumentParser(usage=sys.argv[0]+" [-f] path/to/dir [-n] name [-c] counter")
parser.add_argument('-n', '--name', 
                    default="DSC", 
                    help="New name of the files. Default name is DSC")
parser.add_argument('-c', '--counter',
                    default=1,
                    help='Number from which program starts adding to the new name. Default value is 1 ')
parser.add_argument('-f', '--file',
                    help="Path to dir with files to rename")

args = parser.parse_args()

try:
  oldNames = os.listdir(args.file)

  if not os.listdir(args.file):
    sys.exit(args.file+" is empty")  
  
  newName = args.name + "_"
  counter = int(args.counter)
  path = args.file
  fileCounter = 0

  for filename in oldNames:
    name, ext = os.path.splitext(path+'/'+filename)
    os.rename(path+'/'+filename, path+'/'+newName+str(counter)+ext)
    
    print("Renaming: "+filename+" to: "+newName+str(counter)+ext)

    fileCounter+=1
    counter+=1

  print(str(fileCounter)+" files renaming successfully done!")

except OSError:
  print("Cannot open "+args.file)

except IndexError:
  print("Incompleted argument list")




