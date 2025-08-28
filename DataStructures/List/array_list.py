def new_list():
    
    new_list = {
        "elements": [],
        "size": 0,
    }
    return new_list

def get_element(my_list, index):
    
    return my_list["elements"][index]

def is_present(my_list, element, cmp_function):
    
    size = my_list["size"]
    if size == 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if cmp_function(info, element) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1

def add_first(my_list, element):
    my_list["elements"].insert(0, element)
    my_list["size"] += 1

def add_last(my_list, element):
    my_list["elements"].append(element)
    my_list["size"] += 1
    
def size(my_list):
    return my_list["size"]

def first_element(my_list):
    if my_list["size"] > 0:
        return my_list["elements"][0]
    else:
        return None

def last_element(my_list):
    if my_list["size"] > 0:
        return my_list["elements"][-1]
    else:
        return None

def remove_first(my_list):
    if my_list["size"] > 0:
        my_list["elements"].pop(0)
        my_list["size"] -= 1

def remove_last(my_list):
    if my_list["size"] > 0:
        my_list["elements"].pop()
        my_list["size"] -= 1

def insert_element(my_list, index, element):
    if index >= 0 and index <= my_list["size"]:
        my_list["elements"].insert(index, element)
        my_list["size"] += 1
    