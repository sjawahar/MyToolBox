import ntpath
import os
import constants

cmd = 'cloc '
#for files in constants.pathlist_8123:
    #fname = ntpath.basename(files) 
    #print(fname[:-5])
    #print(os.system(cmd + files))


set822 = set()
set821 = set()

set8123 = set()
set8121 = set()


for files in constants.pathlist_8123:
    set8123.add(files)

for files in constants.pathlist_8121:
    set8121.add(files)

for files in constants.pathlist_822:
    set822.add(files)

for files in constants.pathlist_821:
    set821.add(files)

#print(set8121.difference(set8123))

#diff = set8121.difference(set8123)
diff = set821.difference(set822)

for fname in diff:
    filename = ntpath.basename(fname)
    print(filename[:-5])
    #print(os.system(cmd + fname))