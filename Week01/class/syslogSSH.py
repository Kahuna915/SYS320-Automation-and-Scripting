import syslogcheck
import importlib
importlib.reload(syslogcheck)
# SSH authentication failures
def ssh_fail(filename, searchTerms):

        # call syslogcheck and return the result
        is_found = syslogcheck._syslog(filename,searchTerms)

        # Found list
        found = []

        # Loop through the results
        for eachFound in is_found:
            # split the results
            sp_results = eachFound.split(" ")
            # Append the split value to the found list
            found.append(sp_results[8])
        #Remove duplicates
        # and convert the list to a dictionary
        hosts = (set(found))
        for eachhost in hosts:
            print(eachhost)