import re
def token_parser(s):
    
    tokens = re.findall(r'\d+|[-+*/()]', s)
    return tokens