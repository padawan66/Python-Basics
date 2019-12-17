def mean(mylist):
    the_mean = sum(mylist)/ len(mylist)
    return the_mean

print( "Mean:",mean([1,2,3]), "Type:",type(mean))

def lengther(mylist):
    return len(mylist)

print("lengther:",lengther([1,2,3]))