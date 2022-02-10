# File to traverse a given directory and it's subdirs and retrieve all the files.

import os, argparse, yaml

# Parser
parser = argparse.ArgumentParser(
    description="Traverses a directory and builds a forensic body file"
                "You can use search terms with the associated yaml playbook",
    epilog="Developed by Noah Stiles, 20221002"
)
# Add argument to pass to the fs.py program
parser.add_argument("-d", "--directory", required="True", help="Directory that you want to traverse.")
parser.add_argument("-b, "--" ")

# Parse the arguments
args = parser.parse_args()
rootdir = args.directory



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

def search(path, book, term):
    # query yaml file for the 'term' associated with the book
    terms = attacks[book][term]
    keyattacks = terms.split(",")
    with open(path) as f:
        contents = f.readlines()

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

    def statFile(toStat):
        # i is going to be the variable used for each of the metadata elements
        i = os.stat(toStat,follow_symlinks=False)

        # mode
        mode = i[0]

        # inode
        inode = i[1]

        # uid
        uid = i[4]

        # gid
        gid = i[5]

        #file size
        fsize = i[6]

        # access time
        atime = i[7]

        # modification time
        mtime = i[8]

        # ctime => windows is the birth of the file, when it was created
        # unix it is when attributes of the file changes
        ctime =i[9]
        crtime = i[9]

        print("0|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}".format(toStat, inode, mode, uid, gid, fsize, atime, mtime, ctime, crtime))

    for eachFile in flist:

        statFile(eachFile)
