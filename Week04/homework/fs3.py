# File to traverse a given directory and it's subdirs and retrieve all the files.

import os, argparse, yaml, re,  sys




parser = argparse.ArgumentParser(
    description="Traverses a directory and builds a forensic body file",
    epilog="Developed by Noah Stiles, 20221002"
    )
# Add argument to pass to the fs.py program
parser.add_argument("-d", "--directory", required="True", help="Directory that you want to traverse.")
parser.add_argument("-s", "--service", required="True", help="Yaml book you want to use to search the log files.")
parser.add_argument("-w", "--webvalue", required="True", help="Yaml book you want to use to search the log files.")

# Parse the arguments
args = parser.parse_args()
rootdir = args.directory
service = args.service
webvalue = args.webvalue
# Check if the argument is a directory
if not os.path.isdir(rootdir):
    print("Invalid Directory => {}".format(rootdir))
    exit()

# Open yaml file
try:
    with open('attacks.yaml','r') as yf:
        attacks = yaml.safe_load_all(yf)
            #print(searchterm)
except EnvironmentError as e:
    print(e.strerror)

# List to save files
flist =[]

# Crawl through the provided directory
for root, subfolder, filenames in os.walk(rootdir):
    for f in filenames:
        fileList = root + f
        flist.append(fileList)

result = []
#print(flist)
def searchterms(flist, service, webvalue):
    #print(flist)

    try:
        #for each_file in flist:
            #print(each_file)
            with open(flist) as f:
                contents = f.readlines()  # reads every line of the files
            #print(contents)
            for keyVal in attacks:
                searchterm = keyVal[service][webvalue]
                print(searchterm)
                for line in contents:

            #print(line)
            # loop through the list returned for the keyterms
                    for eachsearchterm in searchterm:
                        x = re.findall(r'' + eachsearchterm + '', line)
                        for found in x:
                            result.append(found)
                            print(result)
    except EnvironmentError as g:
        print(g.strerror)

for eachfile in flist:
    searchterms(eachfile, service, webvalue)

'''
        for found in x:
            slist.append(found)
            #print(slist)
#Check to see if there are results
    if len(slist) == 0:
        print("No Results")
        sys.exit(1)
# sort the list
    results = sorted(slist)
    #print(results)


#Allows us to grab all of the files

def searchterms(flist, service, webvalue):
    print(service)
    #print(webvalue)
    #print(flist)
    for keyVal in attacks:
        searchterm = keyVal[service][webvalue]
        print(searchterm)



    try:
        for each_file in flist:
            with open(each_file, "r") as f:
                contents = f.readlines() # reads every line of the files
                print(contents)
    except EnvironmentError as g:
        print(g.strerror)
    slist = []
                    # loop through the files line by line
                        for line in contents:
                            #print(flist)
                                # loop through the list returned for the keyterms
                            for eachsearchterm in searchterm:
                                #print(searchterm)
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
'''



