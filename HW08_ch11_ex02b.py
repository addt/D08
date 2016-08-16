#!/usr/bin/env python3
# HW08_ch11_ex02b
# This borrows from exercise two in the book.
# Dictionaries have a method called keys that returns the keys of the
# dictionary, in no particular order, as a list.

# (1) Modify print_hist_old to print the keys and their values in alphabetical
# order.

# (2) Paste in your completed functions from HW08_ch11_ex02a.py

# (3) Within main() make the appropriate function calls to print the
# alphabetical histogram of pledge.txt
###############################################################################
# Imports


# Body
def print_hist_old(h):
    for c in sorted(h,  key = str.lower):
        print(c, h[c])


def print_hist_new(h):
    for c in sorted(h,  key = str.lower):
        print(c, h[c])


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

def main():
    """ Calls print_hist_new with the appropriate arguments to print the
    histogram of pledge.txt.
    """
    print_hist_new(histogram_new(get_pledge_list()))

if __name__ == '__main__':
    main()
