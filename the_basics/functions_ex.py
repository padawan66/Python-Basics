def mean(mylist):
    the_mean = sum(mylist)/ len(mylist)
    return the_mean

#print( "Mean:",mean([1,2,3]), "Type:",type(mean))

def lengther(mylist):
    return len(mylist)

#print("lengther:",lengther([1,2,3]))


# below section tells us about the named , keyword arguments default values to the parameters in a 
# function

def test_function(a,b) :
    return a*b

def test_function_default(a,b=8) :
    return a*b

test_function(a=7, b=6) 
test_function(b=7, a=6)  # here the order is not important since the keyword arguments  are used
test_function(7, 4)  # here the order is important


#test_function_default(a=4) # this works since b has a default value defined in the function definition


# Below section shows the way to create function with arbitrary number of arguments ( like print function)

def test_arbitrary(*args):
    return type(args)  # this returns a tuple

#print(test_arbitrary([5,6.8]))

def get_average(*args):
    return (sum(args)/len(args))

#print(get_average(8,9))

def upper_and_sort(*args):
    lst = list(args)
    lst.sort(reverse = False)
    return  [str(item).upper() for item in lst]

def upper_and_sort_optimum(*args):
    args = [x.upper() for x in args]
    return  sorted(args)


# This gives the keword arguments 
# An **kwargs parameter allows the function to be called with an arbitrary number of keyword arguments:
def find_sum(**kwargs):
    return sum(kwargs.values())
    
print(find_sum(a=5,b=4))

print(upper_and_sort_optimum("snow","glaciar","iceberg"))


