

def open_file():
    filename = input("Input filename. > ")
    open_text = open(filename, 'r')
    print("Opened " + filename)
    return open_text 

def parse_file(blarg):
    word_lst = []
    for line in blarg:
        raw_output = line.split() # these are lists of strings
        for str_ in raw_output: # strings
            #a = str_.lower()
            word_lst.append(str_)
    return word_lst

"""def lst_cleaner(input_):
    clean_lst = []
    remove = ".?!-\'\"*\,()[]:#\/;"
    for item in input_:
        temp_str = ""
        for char in item:
            if char not in remove:
                clean_str = ""
                clean_str += char
            temp_str += clean_str
            clean_lst.append(temp_str)
    return clean_lst
"""
def lst_cleaner(input_):
    clean_lst = {}
    remove = ".?!-\'\"*\,()[]:#\/;"
    for item in input_:
        temp_str = ""
        for char in item:
            if char not in remove:
                clean_str = ""
                clean_str += char
            temp_str += clean_str
            clean_lst[temp_str] = 0
    return clean_lst

    """for item in input:
        if item not in remove:
            clean_str += item
        item = clean_str
    clean_lst.append(item)
    return clean_lst
    """
    
def search_dict(dct):
    """input: a dictionary with keys and 1 values.
       output: a dictionary with keys and counted value
    """
    final_dct = {}
    for word in dct:
        if word in dct:
            final_dct[word] = final_dct.get(word, 1) + 1
        else:
            final_dct.get(word, 1)
    return final_dct    


def main():
    foo = open_file()
    bar = parse_file(foo)
    #print(bar)
    woo = lst_cleaner(bar)
    print(woo)
    #foo1 = search_dict(bar)
#for counts in foo1.values():
#    counts.sort(reverse = True)
    #print(foo1)
    
"""Unit Tests"""

def unit_tests():
    file = open('test.txt', 'r') # loads separate test file
    assert parse_file(file) == {'string' : 0}
    assert search_dict({'string' : 1}) == {'string' : 1}
    file.close()
    print("Passed all tests.")

      
main()    
#unit_tests()

