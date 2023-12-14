
list_data[[1,2,3],[3,4],[5,6]]



def data_preparation(list_data):
    
    new_list = []

    for sublist in list_data:
        if len(sublist) > 2:
            sublist.remove(min(sublist))
            sublist.remove(max(sublist))
        new_list.extend(sublist)
    result = sorted(new_list, reverse = True)
    return result
        

# def data_preparation(list_data):
#     list =[]
#     for i in list_data:
#         for el in i:
#             if len(str(el)) > 2:
#                 el.sort()
#                 el.pop()
#                 el.reverce()
#                 el.pop()
#                 list.extend(str(el))
#             else:
#                 list.extend(str(el))
#     list.sort()
#     list.reverse()
#     return list


def data_preparation(data):
    cleaned_data = []
    for sublist in data:
        if len(sublist) > 2:
            sublist.remove(min(sublist))
            sublist.remove(max(sublist))
        cleaned_data.extend(sublist)
    # Відсортований результат
    result = sorted(cleaned_data, reverse=True)
    return result



#             # new_li = 

# list_data = (a, b, c)
# a = [1,2,3]
# b = [3,4]
# c = [5,6]
# b.extend(c)
# a.extend(b)

# chars.extend(numbers)
# n_data = list_data.extend(list_data)
            # print(list_data)
# def prepare_data(data):
    
#     prepare_data = sorted(data)
    
#     prepare_data1 = prepare_data.pop(0)
#     print(prepare_data1)
#     print(prepare_data)
#     prepare_data2 = prepare_data.reverse()
#     print(prepare_data2)
#     print(prepare_data)
#     prepare_data3 = prepare_data.pop(0)
#     print(prepare_data3)
#     print(prepare_data)
#     new_prepare_data = sorted(prepare_data)
#     print (new_prepare_data)
#     return new_prepare_data

# prepare_data([[1,2,3],[3,4], [5,6]])
