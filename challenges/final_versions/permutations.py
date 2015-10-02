#Permute takes two strings as input and checks whether or not they are 
#permutations of one another.

__author__  = "Kevin Saavedra"

def permute(str1, str2):
    """This function takes in a string and checks whether or not they are 
    permuations of one another. This program is CASE SENSITIVE.

    Example:
    --------
    "Foo", "oFo" --> True
    "Foo", "Bar" --> False
    "Foo", "foo" --> False

    Input:
    ------
    Two strings.

    Output:
    True or False
    """
    str1 = set(str1)
    str2 = set(str2)
    if str1 == str2:
        return True
    else: 
        return False

def permutation_tests():
    assert permute("Foo", "oFo") == True
    assert permute("Foo", "Bar") == False
    assert permute("Foo", "foo") == False

permutation_tests()