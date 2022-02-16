# File to traverse a given directory and it's subdirs and retrieve all the files.

import os, argparse, yaml, re,  sys


# Open yaml file
try:
    with open('attacks.yaml','r') as yf:
        attacks = yaml.safe_load(yf)

except EnvironmentError as e:
    print(e.strerror)

parser = argparse.ArgumentParser(
    description="Traverses a directory and builds a forensic body file",
    epilog="Developed by Noah Stiles, 20221002"
    )
# Add argument to pass to the fs.py program
parser.add_argument("-d", "--directory", required="True", help="Directory that you want to traverse.")
parser.add_argument("-s", "--service", required="True", help="Yaml book you want to use to search the log files.")

# Parse the arguments
args = parser.parse_args()
rootdir = args.directory
service = args.service

# Check if the argument is a directory
if not os.path.isdir(rootdir):
    print("Invalid Directory => {}".format(rootdir))
    exit()

# List to save files
flist =[]

# Crawl through the provided directory
for root, subfolder, filenames in os.walk(rootdir):
    for f in filenames:
        fileList = root + " / " + f
        flist.append(fileList)
#print(flist)

#Allows us to grab all of the files
def searchterms(flist, service):
    searchterm = attacks[service]

    try:
        with open(flist) as f:
            contents = f.readlines() # reads every line of the files
            print(contents)
    except EnvironmentError as g:
        print(g.strerror)
    slist = []


    # loop through the files line by line
    for line in contents:
        # loop through the list returned for the keyterms
        for eachsearchterm in searchterm:
            x = re.findall(r''+eachsearchterm+'', line)
            for found in x:
                slist.append(found)
                print(slist)
    # check to see if there are results
    if len(slist) == 0:
        print("No Results")
        sys.exit(1)
    # sort the list
    results = sorted(slist)
    return results

for eachfile in flist:
    searchterms(eachfile,attacks)



