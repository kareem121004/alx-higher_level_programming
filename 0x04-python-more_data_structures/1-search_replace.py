#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list_new = []
    for i in my_list:
        list_new.append(i)

    for i in range(len(list_new)):
        if list_new[i] == search:
            list_new[i] = replace
    return list_new
