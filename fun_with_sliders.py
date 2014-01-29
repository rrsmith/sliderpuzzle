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
    ss = SliderSearch(3, [4, 1, 2, 3, 0, 5, 6, 7, 8])

    path = ss.search_a_star()
    print_path(path)


if __name__ == '__main__':
    main()
