import os
import os.path
import time

FILE = "9a2ba2abf4b728dd.sav" # RENAME TO DATA KEY TO BE READ FROM!!!
FILE1 = "1f0a58a9e0f84227.sav" # RENAME TO DATA KEY TO BE WRITTEN TO!!!
dats = " "

one = os.path.exists(FILE) # CHECKS TO SEE IF PARENT KEY IS IN DIR

with open(FILE1, 'w') as create: # CREATES THE CHILD KEY
  create.write(dats)
  create.close()


def Scan():
  if one == True:
    with open(FILE, 'rb') as binary_file, open(FILE1, 'rb+') as binary:
      bin = binary_file.read(1008)
      for i in range (5):
        time.sleep(0.1)
        print(bin)
      binary.write(bin)
      binary.close()
      binary_file.close()
      os.system('clear')
      print("Child-Key Created Successfully.")
      time.sleep(3)
      exit()

  else:
    print("Parent-Key Not Found")
    time.sleep(3)
    exit()
Scan()