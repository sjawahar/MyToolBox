# Generating Required Information for HUT Orders

## What is needed for HUT Orders

For HUT orders we need the following things
1. List Files which were modified or created new in 100 commits along with their Lines of Code (LoC) count
2. List of Methods modified in those files

There are several other IQBs for HUT order, full list of IQBs can be found here [HUT IQB](https://docs.google.com/spreadsheets/d/1dxvsLGGHZIbx_2PCZ7gG5oIUo0SpXhESQgjGuDLdOSk/edit#gid=1458792882)

But this tool here generates files to satisfy requirements 1 and 2 mentioned above.

## System Requirements
* Python 3.5  and above (This code is tested with Python 3.6, but should work with any version 3.5 and above)
* cloc tool needs to be installed and should be in PATH. check out [cloc tool](http://cloc.sourceforge.net/) for installing cloc
* git must be installed and should be in PATH
* Platform Independent. Tested on Windows 10, but should work on other platforms as well, where python is supported

## Configuring the tool
* There are 3 things you can configure. repository and branches,Language file extensions, number of commits.
* Edit the file ProjectConfigs.py. Configure the values as needed. The fields are self explanatory
* Note that you can give as many repositories as you want and also as many brnaches as you want per repository. The tool will scan all the repositories and their branches and generate necessary files

## Running the tool
* clone this repository
* From inside the root folder run "python OrderGenerator.py"

## Outputs
This tool generates 2 files for each repository and its branch. One file has list of modified file names having the configured file extension for the last n number of commits with their Loc. This file is in CSV format (filename,LoC). The other file is plain text file which has list of classes and the changed methods.

### Example
Suppose you have configured 2 repositories repo1 and repo2 and configured 2 branches in each repository develop and master, then the following files will be generated

#### Inside repo1 directory
* develop_hut_LoC.csv
* develop_hut_changedmethods.txt
* master_hut_LoC.csv
* master_hut_changedmethods.txt

#### Inside repo2 directory
* develop_hut_LoC.csv
* develop_hut_changedmethods.txt
* master_hut_LoC.csv
* master_hut_changedmethods.txt

## Submitting the HUT Orders
Once you have generated the required files and all other IQBs of HUT are done, then you can share these files with the HUT team. You can create a xlsx file from the CSV and you can provide the links to the txt file in the same xlsx sheet and share it with the HUT team.

## Disclaimer and Warning
* The changed method txt file, sometimes have some gargabe text in there , this is due to very simple regex used in this tool. So you may have to clean it up before sharing with HUT team.
* This tool is tested only on my personal machine and its does not have any error handling as such, so please let me know in case it fails
* Feel free to modify the code or fork the repository. 
