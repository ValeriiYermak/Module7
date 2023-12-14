def get_employees_by_profession(path, profession):

    employees_list = []

    with open(path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.find(profession) != -1:
                employees_list.append(line.strip("\n"))
    result = "".join(employees_list).replace(profession,"")
    result = result.strip()
    print(employees_list)
    print(result)
    print(type(result))
    return result

    
        
    
 