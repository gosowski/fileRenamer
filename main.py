import os
import sys

argNumber = len(sys.argv)

if argNumber >= 2:
  newName = sys.argv[2] + "_"
  counter = int(sys.argv[3])
  path = sys.argv[1]
  names = os.listdir(path)
  
  for filename in names:
    os.rename(path+'/'+filename, path+'/'+newName+str(counter))
    counter+=1
    
else:
  print("Bye!")



