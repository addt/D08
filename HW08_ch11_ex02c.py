#!/usr/bin/env python3
# HW08_ch11_ex02c.py
# (1) Modify reverse_lookup_old so that it builds and returns a list of all
# keys that map to v, or an empty list if there are none.

# (2) Paste in your completed functions from HW08_ch11_ex02a.py

# (3) Do not edit what is in main(). It should print what is returned, a list
# of the keys that map to the values passed.
###############################################################################
# Imports


# Body
def reverse_lookup_old(d, v):
    reverse_list = []
    for k in d:
        if d[k] == v:
            reverse_list += [k]
    return reverse_list


def reverse_lookup_new(d, v):
    reverse_list = []
    for k in d:
        if str(d[k]) == v:
            reverse_list = reverse_list + [k]
    return reverse_list


def histogram_new(s):
    d = dict()
    for i in s:
        d[i] = d.get(i,0) + 1
    return d
    


def get_pledge_list():
    """ Opens pledge.txt and converts to a list, each item is a word in
    the order it appears in the original file. returns the list.
    """
    words_list = []
    file_handle = open('pledge.txt','r')
    for i in file_handle.readlines():
        for j in i.split():
            words_list += [j]
    return words_list

def main():   # DO NOT CHANGE BELOW
    pledge_histogram = histogram_new(get_pledge_list())
    print(reverse_lookup_new(pledge_histogram, "1"))
    print(reverse_lookup_new(pledge_histogram, "9"))
    print(reverse_lookup_new(pledge_histogram, "Python"))

if __name__ == '__main__':
    main()
