# File to traverse a given directory and it's subdirs and retrieve all the files.

import os, argparse, yaml



# Parser
import re

parser = argparse.ArgumentParser(
    description="Traverses a directory and builds a forensic body file",
    epilog="Developed by Noah Stiles, 20221002"
)
# Add argument to pass to the fs.py program
parser.add_argument("-d", "--directory", required="True", help="Directory that you want to traverse.")
parser.add_argument("-b", "--book", required="True", help="Yaml book you want to use to search the log files.")
parser.add_argument("-a", "--attack", required="True", help="Attack you would to search for.")
# Parse the arguments
args = parser.parse_args()
rootdir = args.directory
book = args.book
attack =args.attack

# Check if the argument is a directory
if not os.path.isdir(rootdir):
    print("Invalid Directory => {}".format(rootdir))
    exit()

# Open yaml file
try:
    with open('attacks.yaml','r') as n:
        attacks = yaml.safe_load(n)
except EnvironmentError as e:
    print(e.strerror)

def logs(rootdir, book, attack):
    # query the yaml file for the attack and book
    searchterm = attacks[book][attack]
    keywords = searchterm.split(",")

    with open(rootdir) as f:
        contents = f.readlines()
    slist =[]

    # loop through the files line by line
    for line in contents:
        # loop through the list returned for the keyterms
        for eachsearchterm in keywords:
            x = re.findall(r''+eachsearchterm+'', line)
            for found in x:
                slist.append(found)




# List to save files
flist =[]


# Crawl through the provided directory
for root, subfolder, filenames in os.walk(rootdir):
    for f in filenames:

        #print(root +"  " + "|" + "  " + f)
        fileList = root + "/" + f
        #print(fileList)
        flist.append(fileList)

#print(flist)
