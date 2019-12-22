
#We don't have to do an append for each item in the list inside a forloop to create another list we can use inline for loop using 
# list comprehension

# this section contains only with if condition
temps = [221,234,320,230]
new_temps = [temp/100 for temp in temps]
#print(new_temps)


temps = [221,234,320,230]
new_temps = [temp/100 for temp in temps if temp>222]
#print(new_temps)

def return_only_int (input_list):
    return [item for item in input_list if isinstance(item,int)]
    
#print (return_only_int([99,'no data',95,94,'no data']))

def return_only_int (input_list):
    return [item for item in input_list if item>0]
#print (return_only_int([99,-8,95,94,-76]))



#this section contains if else conditions as well


def return_only_int (input_list):
    return [item  if item>0 else "this is wrong" for item in input_list]
#print (return_only_int([99,-8,95,94,-76]))


def return_only_int (input_list):
    return [item  if isinstance(item,int) else 0 for item in input_list]
#print (return_only_int([99,'no data',95,94,'no data']))


def return_only_int (input_list):
    sum_value = 0
    input_float_list = [float(item) for item in input_list]
    for item in input_float_list:
        sum_value +=item
        print(item, ":", sum_value)
    return sum_value
return_only_int(['-0.2','0.0','0.5'])




