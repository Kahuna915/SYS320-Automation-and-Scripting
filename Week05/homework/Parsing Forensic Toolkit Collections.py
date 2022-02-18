import argparse
import os
import yaml


# Let's go through the directory and grab the files
def do_we_have_files(directory):
# But first make sure that the directory is valid
# Check if the argument is a directory
    if not os.path.isdir(directory):
        print("Invalid Directory => {}".format(directory))
        exit()
    # List to save files
    flist = []
    #print(flist)
    # Crawl through the provided directory
    for root, subfolder, filenames in os.walk(directory):
        for f in filenames:
            fileList = root + "\\" + f
            flist.append(fileList)
    return flist



def load_yaml_rules(rules):
    rlist = []
    # Open yaml file

    with open('hwrules.yaml','r') as yf:
        try:
            dict = yaml.safe_load_all(yf)
            #print(dict)
            for keyval in dict:
                #print(keyval)
                rlist = rlist.append(keyval[rules])
        except EnvironmentError as e:
            print(e.strerror)
            return rlist


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Traverses a directory and builds a forensic body file",
        epilog="Developed by Noah Stiles, 20221002"
    )
    # Add argument to pass to the fs.py program
    parser.add_argument("-d", "--directory", required="True", help="Directory that you want to traverse.")
    parser.add_argument("-a", "--attack", required="True", help="Yaml book you want to use to search the log files.")
    # parser.add_argument("-w", "--webvalue", required="True", help="Yaml book you want to use to search the log files.")

    # Parse the arguments
    args = parser.parse_args()
    rootdir = args.directory
    rootattack = args.attack
    #webvalue = args.webvalue

# Call our function to grab all the files
    files = do_we_have_files(rootdir)
    #print(files)

# Supposed to grab the key searchterm from the yaml book
# Hits a unicode Decode Error
    attack = load_yaml_rules(rootattack)
    #print(attack)