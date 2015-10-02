# This script takes in a string and checks to see if it comprised of unique 
# characters.

__author__ = "Kevin Saavedra"

def break_string(string_input):
    """Breaks an input string into a list of characters."""
    lst = []
    for char in string_input:
        lst.append(char)
    return lst


def string_count(lst_input):
    """Counts every character in an input list."""
    count_lst = []
    for char in lst_input:
        counts = lst_input.count(char)
        count_lst.append(counts)
    count_lst.sort(reverse = True)
    return count_lst

def check_unique(count_input):
    """Checks to see whether or not every item in a list is unique."""
    for item in count_input:
        if item > 1:  
            return False
        else:      
            return True

def unique_chars(string):
    """The main function, takes an input string and checks to see if it is 
    comprised of unique characters.

    Example:
    --------
    "Foo" ---> False
    "Bar" ---> True 

    Input:
    ------
    A string.

    Output:
    -------
    True or False.
    """
    str_to_lst = break_string(string)
    counted = string_count(str_to_lst)
    final = check_unique(counted)
    print(final)
    string = input("Type in a string. > ")
    unique_chars(string)


"""Test functions"""
def unique_tests():
    assert break_string('foo') == ['f', 'o', 'o']
    assert string_count(['f', 'o', 'o']) == [2, 2, 1]
    assert check_unique([2, 2, 1]) == False


unique_tests()

if __name__ == "__main__":
    string = input("Type in a string. > ")
    unique_chars(string)
