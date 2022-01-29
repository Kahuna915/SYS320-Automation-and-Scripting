import logcheck2
import importlib
importlib.reload(logcheck2)
# SSH authentication failures
def proxy(filename, service, term):

        # call syslogcheck and return the result
        is_found = logcheck2.logs(filename, service, term)

        # Found list
        found = []

        # Loop through the results
        for eachFound in is_found:
            # split the results
            sp_results = eachFound.split(" ")
            # Append the split value to the found list
            found.append(sp_results[0] + " " + sp_results[2] + " " + sp_results[4] + " " + sp_results[5] + " " + sp_results[6] + " " + sp_results[7] + " " + sp_results[8] + " " + sp_results[9])
        #Remove duplicates
        # and convert the list to a dictionary
        getValues= (set(found))
        for eachValue in getValues:
            print(eachValue)