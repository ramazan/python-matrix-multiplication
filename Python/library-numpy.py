#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy

from optparse import OptionParser


def read(filename):
    lines = open(filename, 'r').read().splitlines()
    A = []
    B = []
    matrix = A
    for line in lines:
        if line != "":
            matrix.append(map(int, line.split("\t")))
        else:
            matrix = B
    return A, B


def print_matrix(matrix):
    matrix = numpy.array(matrix)
    for line in matrix:
        print("\t".join(map(str, line)))


if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-i",
                      dest="filename",
                      default="2000.in",
                      help="input file with two matrices",
                      metavar="FILE")
    (options, args) = parser.parse_args()

    A, B = read(options.filename)
    A = numpy.matrix(A)
    B = numpy.matrix(B)
    C = A * B  # easy and intuitive, isn't it?
    print_matrix(C)
