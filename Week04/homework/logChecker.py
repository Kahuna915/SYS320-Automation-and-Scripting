import re, yaml


def searchterms(filename, services):
    # Opens yaml file
    with open('attacks.yaml', 'r') as yf:
        attacks = yaml.safe_load_all(yf)
        keywords = []

        for KeyVal in attacks:
            for key, value in KeyVal[services].items():
                keywords.append(value)
        with open(filename) as e:
            contents = e.readlines()
        each_result = []

        for line in contents:
            for eachKey in keywords:
                x = re.findall(r'.*'+eachKey+'.*', line)
                for found in x:
                    each_result.append(found)
        if len(each_result) == 0:
            print( "No Results try again")
        each_result = sorted(each_result)
        return each_result


