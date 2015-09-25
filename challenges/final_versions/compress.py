# Takes a string of characters and compresses it.
# Usage: run from python interpreter
__author__    = "Kevin Saavedra"


def compress_string(string):
    """Takes an input string and compresses it by replacing repeated sequential
    characters with the number of times they appear. 
    
    Example:
    --------
    AAABBCCC --> 'A3B2C3'
      
    If a the length of a compressed string is not any longer than the original
    string, then the original sequence is maintained. 
    
    Example:
    --------
    AABBCC --> A2B2C2 --> AABBCC
    
    Parameters
    ----------
    Input:
    string: a string of characters.
    
    Output:
    compress_final: A compressed string.
    """
 
    if string is None: # If no input, returns None.
        return None
    
    elif string == "": # If empty string, returns empty string.
        return ""  
    
    else:
        lst = list(string)
        n = len(lst)
        comp_lst = []

        for index in range(n): 
            if lst[index] != lst[index-1]: # Searches for unequal sequential 
                                           # values.
                count = lst.count(lst[index]) 
                comp_lst.append(lst[index])
                comp_lst.append(count)
              
        final_lst = ''.join(str(str_index) for str_index in comp_lst)

        if len(final_lst) <= len(lst): # If final length equals the final 
                                       # compressed length, defers to the
                                       # original string.
            strg_lst = ''.join(str(str_index) for str_index in lst)
            final = str(strg_lst)
            return final
          
        else:
            compress_final = str(final_lst)
            return compress_final


