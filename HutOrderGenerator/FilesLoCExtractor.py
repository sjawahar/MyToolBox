import subprocess
import xml.etree.ElementTree as ET
import re
import ProjectConfigs



def gen_hut_locfile(chksum_list,fname):
    file_list = get_changed_files(chksum_list)
    filtered_filelist = filter_fileextensions(file_list)
    write_orderfile(filtered_filelist,fname)

def get_changed_files(chksum_list):
    sproc = subprocess.Popen(['python', 'CommandDefs.py', 'get_commitfiles'] + chksum_list, stdout=subprocess.PIPE)
    unique_filelist= set()
    while True:
        line = sproc.stdout.readline()
        if line != b'':
            unique_filelist.add(line.decode('utf-8', 'replace').rstrip())
        else:
            break
    return list(unique_filelist)

def filter_fileextensions(file_list):
    filtered_list = []
    for file in file_list:
        for extn in ProjectConfigs.lang_extn:
            found = re.search(extn+"$",file)
            if found is not None:
                filtered_list.append(file)
                break
    return filtered_list

def write_orderfile(filtered_list,fname):
    with open(fname,'w') as outfile:
        for file in filtered_list:
            Loc = get_LoC(file)
            str = file + ',' + Loc + '\n'
            outfile.write(str)


def get_LoC(file):
    xml_str=[]
    LoC=0
    sproc = subprocess.Popen(['python', 'CommandDefs.py', 'get_loc', file], stdout=subprocess.PIPE)
    while True:
        line = sproc.stdout.readline()
        if line != b'':
            xml_str.append(line.decode('utf-8','replace').strip())
        else:
            break
    xml_str = ''.join(xml_str).strip()
    try:
        root = ET.fromstring(xml_str)
        LoC = root.find('.//total').attrib['code']
    except ET.ParseError:
        LoC = "NA"
    finally:
        return LoC


