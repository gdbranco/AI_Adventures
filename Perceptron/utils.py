"""
Utility functions needed for the project
"""
def mapping(value, istart, istop, ostart, ostop):
    """Maps value from istart to istop to ostart to ostop"""
    return ostart + (ostop - ostart) * ((value - istart) / (istop - istart))
def sign(num):
    return 1 if num >= 0 else -1
def f(x):
    return .3*x + .2