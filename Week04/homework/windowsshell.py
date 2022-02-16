import fs3
def win_events(flist,book, attack):
    is_found = fs3.searchterms(flist, book)
    # Found list
    found = []

    # Loop through the results
    for eachFound in is_found:
        # split the results
        sp_results = eachFound.split(" ")
        # Append the split value to the found list
        found.append(sp_results[3] + " " + sp_results[0] + " " + sp_results[1])
    # Remove duplicates
    # and convert the list to a dictionary
    getValues = (set(found))
    for eachValue in getValues:
        print(eachValue)