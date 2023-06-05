#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list2 = my_list.copy()
    if idx in range(0, len(my_list)):
        list2[idx] = element
        return list2
    return list2
