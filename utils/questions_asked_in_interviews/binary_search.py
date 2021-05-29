def binary_search(the_list,item):
    first = 0
    last = len(the_list) - 1
    found = False
    while first<=last and not found:
        mid = int((first + last)/2)   #or (first+last)//2  // is called floor division operator
        if item==the_list[mid]:       # and there is no ceil operator, we need to import math and
            found = True              # use math.ceil()
            break
        elif item<the_list[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return found

the_list = [0, 2, 3, 5, 7]
item = 2
if binary_search(the_list,item):
    print("The item is in the list")
else:
    print("The item is not in the list")
