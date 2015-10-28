# This function converts a string of consonant-vowel pairs and converts them to
# their original PIN numbers. 

__author__ = "Kevin Saavedra"

def list_consonants(codeword):
    """
    Takes in a codeword and breaks it up into a list of consonant index values.
    """
    con_pin = []
    for char in range(0, len(codeword), 2): #Starting at index 0, every other letter 
                                     #is a consonant.
        con = codeword[char] # This is a string of only consonants. 
        con_index = codeword.index(con) 
        con_pin.append(con_index)
    return con_pin
    
def list_vowels(codeword):
    """
    Takes in a codeword and breaks it up into a list of consonant index values.
    """
    vow_pin = []
    for char in range(1, len(codeword), 2):
        vow = codeword[char] # This is a string of only vowels.
        vow_index = codeword.index(vow) 
        vow_pin.append(vow_index)
    return vow_pin

def final_pin(con_pin, vow_pin):
    fin_pin = []
    for item in range(len(con_pin)): # Calculate the original 2-digit integers
                                     # using the formula a = qm + r
        q = con_pin[item]
        m = 5
        r = vow_pin[item]
        calc_pin = q * m + r
        fin_pin.append(calc_pin)
        
    final_lst = [] 
    for item in fin_pin: 
        if item < 10: # In order to create a two-digit number for 
                      # numbers <10, we need to insert a '0' 
                      # in front of the digit.
            item = '0' + str(item) 
        else:
            final_lst.append(item)
    
    return final_lst
  
def convert_word(word):
    """
    The main function; takes word comprised of consonant-vowel pairs and converts 
    them to their original PIN numbers. 
    
    Note: This function uses the formula a = qm + r to solve for the 
    original value of the PIN number.
    
    Example:
    --------
    'lohi' --> 4327
    'canosi' --> 2055372    
    
    Parameters
    ----------
    Input:
    word: a word comprised of consonant-vowel pairs.
    
    Output:
    A PIN number.
    """

    if word is None: # An empty word returns an error.
        return ValueError

    elif type(word) is int: # Ints will return an error. 
        return ValueError

    CONSONANTS = "bcdfghjklmnpqrstvwyz" 
    VOWELS = "aeiou"
    con_lst = list(CONSONANTS)
    vow_lst = list(VOWELS) 
    
    u_word = str(word)
    length = len(u_word)
    consonants = list_consonants(u_word)
    vowels = list_vowels(u_word)
    final = final_pin(consonants, vowels)
    final_string = ''.join(str(e) for e in final) # The output string
    print(final_string)


"""Function tests"""
def convert_word_test():
    assert list_consonants('lohi') == [4,2]
    assert list_vowels('lohi') == [3,7]
    assert convert_word('lohi') == "4327"
    assert convert_word('canosi') == "5102055372"

convert_word_test()    