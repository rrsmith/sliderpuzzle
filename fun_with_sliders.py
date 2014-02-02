#!/usr/bin/python
#
# Playing around with the slider puzzle search solution/s
#

from slider_search import SliderSearch


def print_path(path):
    if path is None:
        print "No solution found!"
    else:
        if len(path) < 50:
            print path
        print len(path)

def main():
    
    hard = [4, 1, 2, 3, 0, 5, 6, 7, 8]
    wat = [4, 1, 2, 0, 3, 5, 6, 7, 8]
    wat2 = [0, 1, 2, 4, 3, 5, 6, 8, 7]
    moder = [0, 1, 2, 5, 4, 3, 6, 8, 7]
    hmm = [4, 8, 5, 7, 6, 1, 0, 2, 3]
    #ss = SliderSearch(3, moder)
    ss = SliderSearch(3, wat2)

    path = ss.search_a_star()
    print_path(path)


if __name__ == '__main__':
    main()
