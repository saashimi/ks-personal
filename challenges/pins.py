#pin_convert.py: Contains the functions convert_pin() and convert_word(),
#which convert integers to readable consonant-vowel strings and back again.  

__author__    = "Kevin Saavedra"


def convert_pin(pin):
    """Takes input PIN numbers and converts them to a string of
    readable letters. This function allows a PIN of any length
    for input.
    
    This function uses lists of consonants and vowels which are indexed
    from 0:19 and 0:4, respectively. For any two-digit integer x // 5, 
    the quotient will be an index for a consonant. For any two-digit integer
    x % 5, the remainder will be an index for a vowel. The result
    will be a readable word.
    
    Example:
    --------
    4327 --> 'lohi'
    2055372 --> 'canosi'    
    
    Parameters
    ----------
    Input:
    pin: a series of integers of any length.
    
    Output:
    strg_output: a readable, pronounceable string of characters.
    """
     
    if pin is None: # An empty pin returns an error.
        return ValueError

    elif type(pin) is str: # A string will return an error. 
        return ValueError
    
    elif pin == 0: # Pin cannot be zero.
        return ValueError
    
    CONSONANTS = "bcdfghjklmnpqrstvwyz" 
    VOWELS = "aeiou" 
    
    con_lst = list(CONSONANTS)
    vow_lst = list(VOWELS)    
    u_pin = str(pin)
    length = len(u_pin)
    
    pin_lst = []
    for char in range(0, length, 2):
        try: # Breaks the pin number up by pairs into a new list.
            pair = (u_pin[char] + u_pin[char + 1])
            pin_lst.append(pair)

        except IndexError:
            pin_lst = [] # If pin number does not divide evenly into pairs,
                         # inserts a 0 before the first integer.
            u_pin = "0" + str(pin)
            for char in range(0, length, 2):
                pair = (u_pin[char] + u_pin[char + 1])
                pin_lst.append(pair)
            
    int_lst = [int(i) for i in pin_lst] 
          
    fin_con_lst = [] # Takes an empty list and populates it with 
                     # corresponding consonant indices.    
    for item in int_lst:
        a = item   
        con_index = a // 5 # Floor division by 5 gives the index to the list
                           # of consonants.
        con_alpha = con_lst[con_index]
        fin_con_lst.append(con_alpha)
        
  
    fin_vow_lst = [] # Takes an empty list and populates it with 
                     # corresponding vowel indices.
    for item in int_lst:
        a = item    
        vow_index = a % 5 # Remainder is the index to the list of vowels.
        vow_alpha = vow_lst[vow_index]
        fin_vow_lst.append(vow_alpha)

    final_lst = [] # A list of the final consonant-vowel pairs
    n = len(fin_con_lst)
    for item in range(n):
        pairs = fin_con_lst[item] + fin_vow_lst[item]
        final_lst.append(pairs)  
    
    strg_output(final_lst)

def convert_word(word):
    """Takes word comprised of consonant-vowel pairs and converts them to 
    their original PIN numbers. 
    
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
    
    con_pin = []
    for char in range(0, length, 2):
        con = u_word[char] # This is a string of only consonants. 
        con_index = con_lst.index(con) 
        con_pin.append(con_index)
    
    vow_pin = []
    for char in range(1, length, 2):
        vow = u_word[char] # This is a string of only vowels.
        vow_index = vow_lst.index(vow) 
        vow_pin.append(vow_index)

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
    
    strg_output(final_lst)
           
def strg_output(final_lst):
    """Prints the final lists generated from convert_pin() or convert_word()
        into an output string. 
    """ 
    final_string = ''.join(str(e) for e in final_lst) # The output string
    print(final_string)
    
