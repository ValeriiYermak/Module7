def encode(data):
    
    if len(data) == 0:
        return []
    
    key = 0
    
    while data[0] == data[key]:
        key = key + 1
        if key >= len(data):
            break    
    return ([data[0]] + [key]) + encode(data[key:])       
