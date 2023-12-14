def capital_text(s):
    result = ""
    capitalize_next = True
    for el in s:
        if capitalize_next and el.isalpha():
            result = result + el.upper()
            capitalize_next = False
        else:
            result = result + el
        if el in [".", "!", "?"]:
            capitalize_next = True
    return result    