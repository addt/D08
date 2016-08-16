#!/usr/bin/env python3
# HW08_ch11_ex02d.py
# (1) Write a more concise version of invert_dict_old.

# (2) Paste in your completed functions from HW08_ch11_ex02a.py

# (3) Update print_hist_new from HW08_ch11_ex02b.py to be able to print
# a sorted version of the dict (print key/value pairs from 0 through the
# largest key values, (and those in between))
# Ex. If d = {1:["this, that"], 3: ["the"]}, it prints:
#    '1: ["this", "that"]'
#    '2:'
#    '3: ["the"]'
###############################################################################
# Imports


# Body
def invert_dict_old(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


def invert_dict_new(d):
    inverse = dict()
    for key in d:
        val = d[key]
        inverse[val] = inverse.get(val, []) + [key]
    return inverse


def print_hist_newest(d):
    for i in range(1, max(d.keys())+1):
        print("'{}:{}'".format(str(i),str(d.get(i,""))))
    

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

def main():  # DO NOT CHANGE BELOW
    pledge_histogram = histogram_new(get_pledge_list())
    pledge_invert = invert_dict_new(pledge_histogram)
    #print(pledge_invert)
    print_hist_newest(pledge_invert)

if __name__ == '__main__':
    main()
