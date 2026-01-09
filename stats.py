def num_words(book):
    strings = len(book.split())
    return strings    

def count_letters(book):
    len_dict = {}
    for char in book.lower():
        if char not in len_dict:
            len_dict[char] =  1
        else:
            len_dict[char] += 1    
    return len_dict  

def get_key(key):
    return key['num'] 
def sorted_list(book):
    dict_s = count_letters(book)
    unsorted_list = []
    for key,value in dict_s.items():
        dict_to_append = {"char" : key, "num": value}
        unsorted_list.append(dict_to_append)
    return sorted(unsorted_list,key = get_key,reverse=True)
    