def open_file():
    """Opens a file.
    Inputs: Prompts a filename from the user.
    Outputs: A text file for parsing.
    """
    filename = input("Input filename. > ")
    open_text = open(filename, 'r')
    print("Opened " + filename)
    return open_text 

def parse_file(input_lst):
    """Opens a file and counts word occurrences.
    Inputs: A text file.
    Outputs: A dictionary with word occurrence counts.
    """
    word_dct = {}
    for line in input_lst:
        raw_output = line.split() # these are lists of strings
        for str_ in raw_output: # strings
            str_ = str_.lower()
            str_ = str_.replace("-", " ")
            str_ = str_.replace("?", "")
            str_ = str_.replace("!", "")
            str_ = str_.replace(",", "")
            str_ = str_.replace("\'", "")
            str_ = str_.replace('\"', "")
            str_ = str_.replace(".", "")
            if str_ not in word_dct:
                word_dct[str_] = 1
            else:
                word_dct[str_] += 1
    return word_dct

def main():
"""The main function, which prompts the user for a text file and outputs the top 50
   most common word occurences.
"""
    import operator
    init_file = open_file()
    opened_file = parse_file(init_file)
    final = sorted(opened_file.items(), key = operator.itemgetter(1), reverse = True)
    for item in range(51):
        print(final[item])
        
"""Unit Tests"""

def unit_tests():
    file = open('test.txt', 'r') # loads separate test file
    assert parse_file(file) == {'string' : 1}
    file.close()
    #print("Passed all tests.")
    
main()    
unit_tests()

