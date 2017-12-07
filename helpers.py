from numpy import loadtxt

def read_input(fname):
    return loadtxt(fname, dtype = int)
