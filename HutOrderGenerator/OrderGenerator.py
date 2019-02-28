import subprocess
import ProjectConfigs
import os
from shutil import copyfile

import FilesLoCExtractor
import ChangedMethodsExtractor

if __name__ == "__main__":
    for key in ProjectConfigs.repository_path.keys():
        copyfile('CommandDefs.py',key+'\\CommandDefs.py')
        os.chdir(key)
        for branch in ProjectConfigs.repository_path[key]:
            print("On Directory " + key, "On Branch " + branch)
            os.system('git.exe checkout ' + branch)
            proc = subprocess.Popen(['python', 'CommandDefs.py', 'get_gitlog'], stdout=subprocess.PIPE)
            chksum_list = []
            while True:
                line = proc.stdout.readline()
                if line != b'':
                    chksum_list.append(line.decode('utf-8','replace').rstrip())
                else:
                    break
            FilesLoCExtractor.gen_hut_locfile(chksum_list,branch+'_hut_LoC.csv')
            ChangedMethodsExtractor.gen_hut_changedmethods(chksum_list,branch+"_hut_changedmethods.txt")
    print('HUT Files Succesfully Generated')

