# first method // manually
def intersection(list_1,list_2):
    new_list = [item for item in list_1 if item in list_2]
    return new_list

list_1 = [1,2,3,5,7,11,13,2,3]
list_2 = [1,3,5,7,9,11,13]
print(intersection(list_1,list_2))

# second method // using intersection() function. it works for sets, not lists.
# we can easily change lists into sets like this:
def return_intersection(list_1,list_2):
    set_1 = set(list_1)
    set_2 = set(list_2)
    return list(set_1.intersection(set_2))  # this statement can be used for more sets as well
new_list = return_intersection(list_1,list_2)
print(new_list)

