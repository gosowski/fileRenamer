import os
import sys

# argNumber = len(sys.argv)

# if argNumber >= 2:
#   newName = sys.argv[2] + "_"
#   counter = int(sys.argv[3])
#   path = sys.argv[1]
#   names = os.listdir(path)
  
#   for filename in names:
#     os.rename(path+'/'+filename, path+'/'+newName+str(counter))
#     counter+=1

# else:
#   print("Bye!")

try:
  oldNames = os.listdir(sys.argv[1])

  if not os.listdir(sys.argv[1]):
    sys.exit(sys.argv[1]+" is empty")  
  
  newName = sys.argv[2] + "_"
  counter = int(sys.argv[3])
  path = sys.argv[1]

  for filename in oldNames:
    os.rename(path+'/'+filename, path+'/'+newName+str(counter))
    counter+=1

  print("Done")

except OSError:
  print("Cannot open "+sys.argv[1])

except IndexError:
  print("Incompleted argument list")




