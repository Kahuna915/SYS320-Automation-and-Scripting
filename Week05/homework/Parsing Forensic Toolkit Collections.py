import argparse
import os
import yaml
import re
### Author: Noah Stiles
### Date 2/22/2022
### Argument Parser through a directory

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
    with open('hwrules.yaml','rb') as yf: #Opens the yaml file
        try:
            rlist = yaml.safe_load(yf) #Stores it as a list
            rlist = rlist[rules] #Looks for the particular book
            rlist = rlist['Detections'] #Grabs the detections section of our book
            #print(rlist)
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
    files = do_we_have_files(rootdir) #Stores the output of our function as files
    #print(files)
    attack = load_yaml_rules(rootattack) #Stores the output of our function as attack
    #print(attack)

    for eachFile in files: # Goes through and grabs each file
        with open(eachFile, 'r',encoding='utf-8') as yf: # Opens each file needed utf-8 or else you get a unicode error
            contents = (yf.readlines()) # Reads the file as lines and stores it as a variable
            #print(contents)
            results = [] # List for our results
            for line in contents: #For each line in contents
                for eachKeyword in attack: #We search for our keyword which is the descripton we set above
                    x = re.findall(r'.*'+eachKeyword+'.*', line) #Prints the entire line when the keyword is found
                    for found in x:
                        #['21,"""C:\\Program Files\\internet explorer\\iexplore.exe"" ",0001FXGSE,iexplore.exe,C:\\Program Files\\internet explorer,4489,lotti.richards']
                        results.append(" Arguments: " + found[68:80] + " Path: " + found[8:53] + " pid " + found[58:68] + " Username "
                                       + found[120:150] + " Hostname: " + found[0:5]) #appends our lists with valuable information

            results = sorted(results) #Sorts our list and prints it


            with open('hwrules.yaml', 'rb') as yf:  # Opens the yaml file
                try:
                    d_rlist = yaml.safe_load(yf)  # Stores it as a list
                    #print(d_rlist)
                    main_book = d_rlist[rootattack]
                    #print(main_book)
                    description = main_book["Description"]  # Looks for the particular book
                    references = main_book["References"]  # Grabs the detections section of our book
                    if len(results) == 1:
                        print(results)
                        print(description, references)
                except EnvironmentError as e:
                    print(e.strerror)




