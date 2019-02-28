import subprocess
import re
import ProjectConfigs
import ntpath

def gen_hut_changedmethods(commit_list,fname):
    proc = subprocess.Popen(['python',  'CommandDefs.py', 'get_fulldiff'] + commit_list, stdout=subprocess.PIPE)
    dlist = []
    while True:
        line = proc.stdout.readline()
        if line != b'':
            str = line.decode('utf-8', 'replace')
            dlist.append(make_list(str))
        else:
            break
    write_file(fname, dlist)

def extract_filename(txt):
    return ntpath.basename(txt[11:])

def filter_filenames(txt):
    found_diff = re.search("diff --git ", txt)
    ret_val = ''
    if found_diff is not None:
        for extn in ProjectConfigs.lang_extn:
            found_ext = re.search(extn+"$", txt)
            if found_ext is not None:
               ret_val = extract_filename(txt)
               break
    return ret_val

def find_methods(txt):
    found_method = re.search("public|private|::",txt)
    if found_method is not None:
        return txt[found_method.start():]
    else:
        return ''

def make_list(txt):
    fstr = ''
    filter_file = filter_filenames(txt)
    method = find_methods(txt)
    if filter_file is not '':
        fstr = '############# '+filter_file
    if method is not '':
        fstr = method
    return fstr

def write_file(fname, data):
    with open(fname,'w', encoding="utf-8") as dfile:
        for item in data:
            dfile.write(item)

