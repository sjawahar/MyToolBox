import subprocess
import xml.etree.ElementTree as ET
import ntpath



def gen_hut_locfile(chksum_list,out_fname):
    file_list = get_changed_files(chksum_list)

    return

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

def get_LoC(file):
    sproc = subprocess.Popen(['python', 'CommandDefs.py', 'get_loc', file], stdout=subprocess.PIPE)
    xml_str=[]
    LoC=0
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


