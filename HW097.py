# def all_sub_lists(data):
    
#     if len(data) == 0:
#         return [[]]
    
    
#     sublists = []
#     first = data[0]
#     remaining = data[1:]
#     sublist_remaining = all_sub_lists(remaining)

#     for sublist in sublist_remaining:
#         sublists.append(sublist + [first])

#     sublists.extend(sublist_remaining)

#     return sublists





    # for i in range(len(data) + 1):
    #     for j in range(i + 1, len(data) + 1):
    #         result_list.append(data[i:j])
    # return result_list
    
    # for i in range(1, len(data) + 1):
    #     for j in range(0, len(data) - i + 1):
    #         new_sublist.append(data[i: i + i])
    #         return new_sublist






    # def all_sub_lists(data):

    # new_sublist = [[]]

    # if not data:
    #     return[[]]
    
    # for i in range(len(data) + 1):
    #     for j in range(i + 1, len(data) + 1):
    #         new_sublist.append(data[i:j])
    # return new_sublist


def all_sub_lists(data):
        
    B = [[ ]] 
    
    for i in range(len(data) + 1):   
        for j in range(i + 1, len(data) + 1):         
            sub = data[i:j] 
            B.append(sub) 
    return sorted(B, key=len) 