import subprocess
import ProjectConfigs
import os
from shutil import copyfile

import FilesLoCExtractor


if __name__ == "__main__":
    for key in ProjectConfigs.repository_path.keys():
        copyfile('CommandDefs.py',key+'\\CommandDefs.py')
        os.chdir(key)
        for branch in ProjectConfigs.repository_path[key]:
            os.system('git.exe checkout ' + branch)
            proc = subprocess.Popen(['python', 'CommandDefs.py', 'get_gitlog'], stdout=subprocess.PIPE)
            chksum_list = []
            while True:
                line = proc.stdout.readline()
                if line != b'':
                    chksum_list.append(line.decode('utf-8','replace').rstrip())

                else:
                    break
            print(FilesLoCExtractor.get_LoC(FilesLoCExtractor.get_changed_files(chksum_list)[0]))
