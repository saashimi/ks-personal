def open_file():
    filename = input("Input filename. > ")
    open_text = open(filename, 'r')
    print("Opened " + filename)
    return open_text 

def parse_file(input_lst):
    word_lst = []
    for line in input_lst:
        raw_output = line.split() # these are lists of strings
        for str_ in raw_output: # strings
            str_ = str_.lower()
            str_ = str_.replace("-", "")
            str_ = str_.replace("?", "")
            str_ = str_.replace("!", "")
            str_ = str_.replace(",", "")
            str_ = str_.replace("\'", "")
            str_ = str_.replace('\"', "")
            str_ = str_.replace(".", "")
            word_lst.append(str_)
    return word_lst

def search_dict(dct):
    """input: a list of words.
       output: a dictionary with keys and counted value
    """
    final_dct = {}
    for word in dct:
        if word in dct:
            final_dct[word] = final_dct.get(word, 0) + 1
    return final_dct    

def main():
    import operator
    init_file = open_file()
    opened_file = parse_file(init_file)
    to_search = search_dict(opened_file)
    final = sorted(to_search.items(), key = operator.itemgetter(1), reverse = True )
    for item in range(51):
        print(final[item])
        
"""Unit Tests"""

def unit_tests():
    file = open('test.txt', 'r') # loads separate test file
    assert parse_file(file) == ['string']
    assert search_dict(['string']) == {'string' : 1}
    file.close()
    #print("Passed all tests.")
    
main()    
unit_tests()

