import re, yaml, os, argparse , sys

# Traverse a directory and search files for key attacks
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
parser.add_argument("-a", "--attack", required="True", help="Attack you would to search for.")
# Parse the arguments
args = parser.parse_args()
rootdir = args.directory
service = args.service
attack = args.attack

# Check if the argument is a directory
if not os.path.isdir(rootdir):
    print("Invalid Directory => {}".format(rootdir))
    exit()

#Allows us to grab all of the files
def searchtermz(files, service, attack):


    # List to save files
    flist = []

    # Crawl through the provided directory
    for root, subfolder, filenames in os.walk(rootdir):
        for f in filenames:
            fileList = root + "/" + f
            flist.append(fileList)
            files = flist
            # print(flist)
            #print(fileList)
    #for files in flist:
        # print(book)
        # query the yaml file for the attack and book
    searchterm = attacks[service][attack]
    keywords = searchterm.split(",")
        # print(keywords)
    with open(files) as f:
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


#if __name__== '__main__':
    #searchtermz()
