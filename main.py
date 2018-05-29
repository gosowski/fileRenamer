import os
import sys

try:
  oldNames = os.listdir(sys.argv[1])

  if not os.listdir(sys.argv[1]):
    sys.exit(sys.argv[1]+" is empty")  
  
  newName = sys.argv[2] + "_"
  counter = int(sys.argv[3])
  path = sys.argv[1]
  fileCounter = 0

  for filename in oldNames:
    os.rename(path+'/'+filename, path+'/'+newName+str(counter))
    print("Renaming: "+filename+" to: "+newName+str(counter))
    fileCounter+=1
    counter+=1

  print(str(fileCounter)+" files renaming successfully done!")

except OSError:
  print("Cannot open "+sys.argv[1])

except IndexError:
  print("Incompleted argument list")




