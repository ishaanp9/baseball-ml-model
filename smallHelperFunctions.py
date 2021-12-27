def rindex(mylist, myvalue):
    return max(index for index, item in enumerate(mylist) if item == myvalue)