# there is a python data structure called set() that doesnt allow duplicate data
# here is how set works:
a_set = set()
a_set.add("Raj Maharjan")
a_set.add("Richard Hendricks")
a_set.add("Erlich Bachman")
a_set.add("Raj Maharjan")
print(a_set)

# lets return duplicates

def get_duplicates(the_list):
    dups = []
    a_set = set()
    for item in the_list:
        length_before = len(a_set)
        a_set.add(item)
        length_after = len (a_set)
        if length_before == length_after:
            dups.append(item)
    return dups

the_list = [1,2,3,4,5,6,7,8,9,0,4,5,6,2,2]
print(get_duplicates(the_list))
