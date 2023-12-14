import re
def solve_riddle(riddle, word_length, start_letter, reverse=False):
    if reverse:
        pattern = f'\w{{{word_length - 1}}}{start_letter}'
        found_data = re.search(pattern, riddle)
        if found_data != None:
            raw_result = found_data.group()
            result = raw_result[::-1]
            return result
    pattern = f'{start_letter}\w{{{word_length - 1}}}'
    found_data = re.search(pattern, riddle)
    if found_data != None:
        result = found_data.group()
        return result
    else:
        return ""