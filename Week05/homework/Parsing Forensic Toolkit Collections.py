import argparse
import os
import yaml
import csv
import re

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
    #print(rlist)
    with open('hwrules.yaml','rb') as yf:
        try:
            hlist = yaml.safe_load(yf)
            rlist = hlist[rules]
            rlist = rlist['Detections']
            #print(rlist)
        except EnvironmentError as e:
            print(e.strerror)
        return rlist

    '''
            for rule in rlist:
                print(rule)
                if rule in rules:
                    rlist = rule
                    print(rlist)

                    return rlist
    '''

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

    for eachFile in files:
        with open(eachFile, 'r',encoding='utf-8') as yf:
            contents = (yf.readlines())
        #print(contents)
        results = []
        for line in contents:
            for eachKeyword in attack:
                x = re.findall(r'.*'+eachKeyword+'.*', line)
                for found in x:
                    results.append(found)
        if len(results) == 0:
            print("No Results")
        results = sorted(results)
        print(results)
            #print(line)
            #if attack in contents:
            #for eachKeyword in attack:
                #x = re.findall(r''+eachKeyword+'', line)
                #print(x)
                #for found in x:
                    #results.append(found)
                    #if len(results) == 0:
                        #print("No Results")
                    #results = sorted(results)
                    #print(results)
'''
    for eachFile in files:
        with open(eachFile, newline='') as e:
            contents = csv.reader(e, delimiter=' ', quotechar='|')
            #print(contents)
        results = []
        for row in contents:
            #print(row)
            for eachKeyword in attack:
                x = re.findall(r''+eachKeyword+'', row)
                for found in x:
                    results.append(found)
                    if len(results) == 0:
                        print("No Results")
                    results = sorted(results)
                    print(results
                          )
            #print(eachFile)
            #contents = csv.reader(e)
            #for line in contents:
                #print(line)
'''

