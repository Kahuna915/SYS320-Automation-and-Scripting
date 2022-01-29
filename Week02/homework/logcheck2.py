# Create interface to search through syslog files
import re, sys, yaml


# open the yaml files
try:
    with open('searchTermshw.yaml','r') as yf:
        keywords = yaml.safe_load (yf)

except EnvironmentError as e:
    print(e.strerror)


def logs(filenane,service, term):
    # query yaml file for the 'term' or direction and
    # retrieve the strings to search on.
    terms = keywords[service][term]
    listOfKeywords = terms.split(",")


    # Open a file
    with open(filenane) as f:

        # read in the file and save it to a variable
        contents = f.readlines()

    # Lists store the results
    results = []

    # Loop through the list returned. Each element is a line from the smallSyslog file
    for line in contents:

        # Loop through the keywords
        for eachKeyword in listOfKeywords:

            # If the line contains a keyword it will print
            #if eachKeyword in line:
            # searches and returns resulsts using a regular expression search
            x = re.findall(r''+eachKeyword+'', line)
            for found in x:
                # append the returned keywords to the results list
                results.append(found)

    #check to see if there are results
    if len(results) == 0:
        print("No Results")
        sys.exit(1)
    # sort the list
    results = sorted(results)


    return results
           # print(x)


