import subprocess
import re
import ntpath


def extractfilename(txt):
    return ntpath.basename(txt[11:])

def findjavafile(txt):
    foundiff = re.search("diff --git ", txt)
    if foundiff is not None:
        found = re.search(".java$", txt)
        if found is not None:
            return extractfilename(txt)
        else:
            return ''
    else:
        return ''

def findmethods(txt):
    foundmethod = re.search("public|private",txt)
    if foundmethod is not None:
        return txt[foundmethod.start():]
    else:
        return ''

def make_list(txt,resset):
    jfile = findjavafile(txt)
    jmethod = findmethods(txt)
    if jfile is not '':
        resset.append(jfile)
    if jmethod is not '':
        resset.append(jmethod)

def write_file(fname, data):
    with open(fname,'w') as dfile:
        for item in data:
            isjava = re.search(".java$",item)
            if isjava is not None:
                dfile.write('############# '+item)
            else:
                dfile.write(item)
    return

proc = subprocess.Popen(['python', 'GitCommandExecutor.py'], stdout=subprocess.PIPE)
fname = 'javamethodlist_8121.txt'
dlist = []

while True:
    line = proc.stdout.readline()
    if line != b'':
        make_list(line.decode('utf-8','replace'),dlist)
    else:
        break

write_file(fname,dlist)
print('file written succesfully')