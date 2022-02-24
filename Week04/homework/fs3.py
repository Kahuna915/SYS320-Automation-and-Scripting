# File to traverse a given directory and it's subdirs and retrieve all the files.
#!/bin/bash
import os, argparse
import logChecker
parser = argparse.ArgumentParser(
    description="Traverses a directory and builds a forensic body file",
    epilog="Developed by Noah Stiles, 20221002"
    )
# Add argument to pass to the fs.py program
parser.add_argument("-d", "--directory", required="True", help="Directory that you want to traverse.")
parser.add_argument("-s", "--service", required="True", help="Yaml book you want to use to search the log files.")
#parser.add_argument("-w", "--webvalue", required="True", help="Yaml book you want to use to search the log files.")

# Parse the arguments
args = parser.parse_args()
rootdir = args.directory
service = args.service
#webvalue = args.webvalue
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

for each_file in flist:
    print("Log Files: " + each_file)
    is_found = logChecker.searchterms(each_file, service)
    results = []
    for each_result in is_found:
        print(each_result)
        results_split = each_result.split(" ")
        results.append("IP: " + results_split[0] + " URL: " + results_split[6] + " Status Codes: " + results_split[8] + " Bytes Returnerd: " + results_split[9])
#print (results)
results = set(results)

#for resultant in results:
    #print(resultant)
'''
#print(flist)
def searchterms(flist, service, webvalue):
    print(flist)

    try:
        #for each_file in flist:
            #print(each_file)
            with open(flist) as f:
                contents = f.readlines()  # reads every line of the files
            #print(contents)
            for keyVal in attacks:
                #print(attacks)
                searchterm = keyVal[service][webvalue]
                #print(searchterm)
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



