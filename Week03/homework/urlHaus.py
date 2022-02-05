#
import csv, re #Imported Re
#
def urlHausOpen(filename,searchTerm): #changed ur1 to url
    with open(filename) as f: #Change while to with & deleted the ''
        contents = csv.reader(f) #stores the file as a variable, changed the == to = and csv to f & review to reader


        for _ in range(9):
            next(contents) #skips the first 9 lines of the file

        for eachLine in contents: # reordered this code so that it looks at each line

            for keyword in searchTerm: #Changed searchTerms to searchTerm & reordered it
                x = re.findall(r''+keyword+'',eachLine[2])  # replaced '+' with '' & added '' after the +

                for _ in x:                         #Indented accordingly
                                                    # Don't edit this line. It is here to show how it is possible
                                                    # to remove the "tt" so programs don't convert the malicious
                                                    # domains to links that an be accidentally clicked on.
                    the_url = eachLine[2].replace("http", "hxxp") #Indented so it would be apart of the for loop
                    the_src = eachLine[7] #Indented so it would be apart of the for loop
                    stars = "*"*60 #added this variable to add * in between

                    print(
                        """
                        URL: {}
                        Info: {} 
                        {}""".format(the_url, the_src, stars)) #Indented so it would be apart of the for loop, changed , to .
                    # added {} on each line cause format take the index and matches it with the {}