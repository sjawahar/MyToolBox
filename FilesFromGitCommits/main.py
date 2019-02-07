import os
import constants

git_cmd = 'git.exe diff-tree --no-commit-id --name-only -r '

os.chdir(r"C:\Users\selva\Projects\xo\KnovaMigrated\Avolin-Knova-Main")

cloc_cmd = 'cloc --csv  --list-file  '

#for commit_hash in constants.commit_8121:
 #  os.system(git_cmd+commit_hash)


cpp_filename = r"C:\Users\selva\Projects\xo\KnovaMigrated\cppfilelist8121.txt"
java_filename = r"C:\Users\selva\Projects\xo\KnovaMigrated\javafilelist8121.txt"
jsp_filename = r"C:\Users\selva\Projects\xo\KnovaMigrated\jspfilelist8121.txt"
js_filename = r"C:\Users\selva\Projects\xo\KnovaMigrated\jsfilelist8121.txt"

filelist = [cpp_filename, java_filename, jsp_filename, js_filename]

for files in filelist:
 os.system(cloc_cmd + files)

#filereader = open('../totaljsfilelist8121','r')

#unique = set()
#for lines in filereader:
#  unique.add(lines)

#for items in unique:
#  print(items[:-1])