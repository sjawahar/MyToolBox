import os
import sys
import constants

git_cmd = 'git.exe diff-tree -p -r '

os.chdir(r"C:\Users\selva\Projects\xo\KnovaMigrated\Avolin-Knova-Main")


for elem in constants.commit_8121:
    os.system(git_cmd + elem)

sys.stdout.flush()