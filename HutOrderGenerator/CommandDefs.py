import os
import sys


def get_gitlog():
    os.system('git log -10 --pretty=format:%h --no-merges')

def get_commitfiles(commit_list):
    for commit in commit_list:
        os.system('git.exe diff-tree --no-commit-id --name-only -r ' + commit)

def get_loc(file):
    os.system('cloc --xml --quiet '+file)


def call_func(args):
    if args[1] == 'get_gitlog':
        get_gitlog()
    if args[1] == 'get_commitfiles':
        get_commitfiles(args[2:])
    if args[1] == 'get_loc':
        get_loc(args[2])

    sys.stdout.flush()

if __name__=='__main__':
    call_func(sys.argv)