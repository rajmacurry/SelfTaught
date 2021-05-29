def count_characters(word):
    word = word.lower()
    count_dict = {}
    for c in word:
        if c in count_dict:
            count_dict[c] += 1
        else:
            count_dict[c] = 1
    print(count_dict)

count_characters("yolo")
