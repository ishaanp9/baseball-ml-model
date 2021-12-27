#collection of small helper functions

#returns last index of a particular value in a list
def rindex(mylist, myvalue):
    return len(mylist) - mylist[::-1].index(myvalue) - 1