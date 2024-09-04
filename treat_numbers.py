import re
def extract_numbers(term):
    denominator = True
    term = term.replace(" ", "")
    # use regex to extract numbers and their signs/separators(+,-,/,*,%)
    pattern = r'-?\b\s*\d+(?:\.\d+)?\b'
    
    matches = [int(match.replace(" ", "")) if '-' in match else int(match) for match in re.findall(pattern, term)]
    # return numbers and their separator eg. "3/7", [3,7,/], "-3*-6" = [-3,-6,*]
    if len(matches) == 1:
        denominator = False
        return matches[0]
    return matches[0], matches[1]