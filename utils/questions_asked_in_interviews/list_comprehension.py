# list comprehension
# allows you to create lists based on criteria applied to existing lists
# can write single statements that can :
# 1)    examines every character in the original string
# 2)    selects digits from a string and put them in a list
# 3)    selects the rightmost digit from the list.

input_string = "Buy 1 get 2 free"
new_list = [c for c in input_string]
print(new_list) # prints every character

new_list = [c for c in input_string if c.isdigit()]
print(new_list) # prints numbers only

new_list = [c for c in input_string if c.isdigit()][-1]
print(new_list) # prints the rightmost number

#syntax: new_list = [expression(i) for i in input_list if filter(i)]
