import re, yaml, os, argparse , sys

if __name__== '__main__':
    parser = argparse.ArgumentParser(
        description="Traverses a directory and builds a forensic body file",
        epilog="Developed by Noah Stiles, 20221002"
    )
    # Add argument to pass to the fs.py program
    parser.add_argument("-d", "--directory", required="True", help="Directory that you want to traverse.")
    parser.add_argument("-s", "--service", required="True", help="Yaml book you want to use to search the log files.")
    parser.add_argument("-a", "--attack", required="True", help="Attack you would to search for.")

    # Parse the arguments
    args = parser.parse_args()

    # Values
    rootdir = args.directory
    service = args.service
    attack = args.attack

# Check if the argument is a directory
if not os.path.isdir(rootdir):
    print("Invalid Directory => {}".format(rootdir))
    exit()

# List to save files
flist = []

# Crawl through the provided directory
for root, subfolder, filenames in os.walk(rootdir):
    for f in filenames:
        fileList = root + "/" + f
        print(fileList)

def searchterms(services):
    slist = []

    # open the yaml files
    with open('attacks.yaml', 'r') as yf:
            attacks = yaml.safe_load(yf)
    #print(attacks)
    for files in flist:
        #print(book)
        # query the yaml file for the attack and book
        searchterm = attacks[service]
        with open(files) as f:
            contents = f.readlines() # reads every line of the files
        #print(contents)
            # loop through the files line by line
    for line in contents:
            # loop through the list returned for the keyterms
        for eachsearchterm in line:
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
if __name__== '__main__':
    searchterms(argparse)



