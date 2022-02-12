# File to traverse a given directory and it's subdirs and retrieve all the files.

import os, argparse, yaml, re, sys

# Parser

parser = argparse.ArgumentParser(
    description="Traverses a directory and builds a forensic body file",
    epilog="Developed by Noah Stiles, 20221002"
)
# Add argument to pass to the fs.py program
parser.add_argument("-d", "--directory", required="True", help="Directory that you want to traverse.")
parser.add_argument("-b", "--book", required="True", help="Yaml book you want to use to search the log files.")
# Parse the arguments
args = parser.parse_args()
rootdir = args.directory
books = args.book


# Open yaml file
try:
    with open('attacks.yaml','r') as yf:
        attacks = yaml.safe_load(yf)

except EnvironmentError as e:
    print(e.strerror)
#print(attacks)





# Check if the argument is a directory
if not os.path.isdir(rootdir):
    print("Invalid Directory => {}".format(rootdir))
    exit()



# List to save files
flist =[]


# Crawl through the provided directory
for root, subfolder, filenames in os.walk(rootdir):
    for f in filenames:
        fileList = root + f
        flist.append(fileList)
        #print(flist)
        #print(fileList)


#Allows us to grab all of the files
def searchterms(flist, books):
    #print(flist)
    searchterm = attacks[books]
    keywords = searchterm.split(",")
    print(keywords)
    with open(flist) as f:
            contents = f.readlines() # reads every line of the files
    slist =[]
    #print(contents)
            #print(slist)
            # loop through the files line by line
    for line in contents:
            # loop through the list returned for the keyterms
        for eachsearchterm in keywords:
            x = re.findall(r''+eachsearchterm+'', line)
            for found in x:
                slist.append(found)
                    #print(slist)
        # check to see if there are results
    if len(slist) == 0:
        print("No Results")
        sys.exit(1)
        # sort the list
    results = sorted(slist)
    return results

#if __name__ == '__main__':
    #searchtermz()
    #print(flist)

for eachfile in flist:
    searchterms(eachfile)