# zip take more than one iterable and combines to form a tuple.

movies = ["Interstellar","The Dark Knight Rises","What Women Want","The Family Man"]
ratings = [10, 10, 7, 7]
new_list = []

for item in zip(movies,ratings):
    new_list.append(item)

print(new_list)

# if the number of elements is not equal, then the zip function will output tuples who exist

movies = ["Interstellar","The Dark Knight Rises","What Women Want","The Family Man"]
ratings = [10, 10,]
new_list = []

for item in zip(movies,ratings):
    new_list.append(item)

print(new_list)
