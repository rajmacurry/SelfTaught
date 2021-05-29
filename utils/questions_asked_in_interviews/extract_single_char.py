the_list = [0,0,1,1,2,3,3,4,4,5,5]
def return_single(the_list):
    dups = []
    a_set = set()
    for item in the_list:
        length_before = len(a_set)
        a_set.add(item)
        length_after = len(a_set)
        if length_before == length_after:
            dups.append(item)
    dups_set = set(dups)
    for item in dups_set:
        a_set.remove(item)
    return list(a_set)

print(return_single(the_list))

# or easy way
numbers = [1, 1, 2, 2, 3, 3, 4, 5, 5]
count = {}
for i in numbers:
    if i not in count:
        count[i] = 1
    else:
        count[i] += 1

for key, value in count.items():
    if value == 1:
        print(key)