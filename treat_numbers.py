import re
def extract_numbers(term):
    term = term.replace(" ", "")
    # use regex to extract numbers and their signs/separators(+,-,/,*,%)
    pattern = r'-?\b\s*\d+(?:\.\d+)?\b'
    
    matches = [int(match.replace(" ", "")) if '-' in match else int(match) for match in re.findall(pattern, term)]
    # return numbers and their separator eg. "3/7", [3,7,/], "-3*-6" = [-3,-6,*]
    return matches[0], matches[1]