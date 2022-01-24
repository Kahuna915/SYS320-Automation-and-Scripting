import re, sys
    # Create interface to search through syslog files
def _syslog(filenane,listOfKeywords):
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


