#
import csv, re #Imported Re
#
def urlHausOpen(filename,searchTerm): #changed ur1 to url
    with open(filename) as f: #Opens the file & deleted the ''
        contents = csv.reader(f) #stores the file as a variable, changed the == to = and csv to f


        for _ in range(9): #changed _ to line and range[9] to contents
            next(contents)

        for eachLine in contents:

            for keyword in searchTerm: #Changed searchTerms to searchTerm
                x = re.findall(r''+keyword+'',eachLine[2])  # replaced + W/'' added '' after the +

                for _ in x:                         #Indented accordingly
                                                    # Don't edit this line. It is here to show how it is possible
                                                    # to remove the "tt" so programs don't convert the malicious
                                                    # domains to links that an be accidentally clicked on.
                    the_url = eachLine[2].replace("http", "hxxp") #Indented so it would be apart of the for loop
                    the_src = eachLine[7] #Indented so it would be apart of the for loop
                    stars = "*"*60

                    print(
                        """
                        URL: {}
                        Info: {}
                        {}""".format(the_url, the_src, stars)) #Indented so it would be apart of the for loop