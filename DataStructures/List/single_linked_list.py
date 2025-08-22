from DataStructures.List import list_node as ns

def new_list():
    newlist = {
        "first": None,
        "last": None,
        "size": None,
    }
    
    return newlist

def add_first(list, element):
    n = ns.new_single_node(element)
    n["next"] = list["first"]
    list["first"] = n
    list["size"] += 1
    return list

def add_last(list, element):
    n = ns.new_single_node(element)
    if list["first"] == None:
        list["first"] = n
    n["next"] = None
    list["last"] = n
    list["size"] += 1
    return list

def size(list):
    return list["size"]

def first_element(list):
    if not(list["first"] == None):
        return list["first"]
    else:
        return None
    