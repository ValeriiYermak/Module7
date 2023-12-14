def flatten(data):
    #data = [1, 2, [3, 4, [5, 6]], 7]
    #output list = [1, 2, 3, 4, 5, 6, 7]
    if not data:
        return []
    
    output_list = []
    for item in data:
        if type(item) == list:
            output_list.extend(flatten(item))
        else:
            output_list.append(item)
    #output_list = flatten(data)
    print(output_list)
    return output_list