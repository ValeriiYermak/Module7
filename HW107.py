def make_request(keys, values):

    dict = {}

    for i in range(len(keys)):
        if len(keys) == len(values):
            dict[keys[i]] = values[i]
    print(dict)
    return dict
    