def create_an_empty_list():
    return []

def create_a_list():
    my_list = []
    my_list.append(3)
    my_list.append('bobs')
    my_list.append('apples')
    my_list.append('six')
    return my_list

my_list = create_a_list()
print(my_list)

def add_element_to_end_of_list(l, element):
    l.append(element)
    return l

def add_element_to_start_of_list(l, element):
    l.insert(0, element)
    return l

def remove_element_from_end_of_list(l):
    if len(l) == 0:
        return l
    else:
        l.pop()
        return l

def remove_element_from_start_of_list(l):
    if len(l) > 0:
        l.pop(0)
    return l

def retrieve_first_element_from_list(l):
    if len(l) > 0:
        return l[0]
    return None

def retrieve_element_from_index(l, index):
    if index < len(l):
        return l[index]
    return None

def retrieve_last_element_from_list(l):
    if len(l) > 0:
        return l[-1]
    return None
