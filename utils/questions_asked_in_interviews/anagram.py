# an anagram are words that can be made from each other. example iceman and cinema
# for this you sort both words in order and check is the sorted is same or not

def is_anagram(w1,w2):
    w1 = w1.lower()
    w2 = w2.lower()
    return sorted(w1) == sorted(w2)

print(is_anagram("iceman","cinema"))
