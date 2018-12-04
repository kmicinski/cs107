# CMSC 107 -- Lecture 1
# Introduction to Python and Basic Recursive Design

empty = []

# Build a list from a number and a tail
def mk_list(head,tail):
    return [head] + tail

def head(lst):
    return lst[0]

def tail(lst):
    return lst[1:]

def gt0(n):
    if (n > 0):
        return True
    else:
        return False

# Uses f as higher order function
def filter(lst,f):
    if (len(lst) == 0):
        return []
    else:
        if (f(head(lst))):
            return mk_list(head(lst),filter(tail(lst),f))
        else:
            return filter(tail(lst),f)

print(gt0(1))

