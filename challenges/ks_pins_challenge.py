 ## Constants used by this program
CONSONANTS = "bcdfghjklmnpqrstvwyz" 
VOWELS = "aeiou" 

def convert_pin(pin):


    if pin is None:
        return ValueError

    elif type(pin) is str:
        return ValueError
    
    elif pin == 0:
        return ValueError
    
    con_lst = list(CONSONANTS)
    vow_lst = list(VOWELS)    
    u_pin = str(pin)
    length = len(u_pin)
    pin_lst = []
    
### Converts a string a list of pairs.  If there are no pairs, 
### inserts a 0 before the leading number.

    for char in range(0, length, 2):
        try:
            pair = (u_pin[char] + u_pin[char + 1])
            pin_lst.append(pair)

        except IndexError:
            pin_lst = []
            u_pin = "0" + str(pin)
            for char in range(0, length, 2):
                pair = (u_pin[char] + u_pin[char + 1])
                pin_lst.append(pair)

### Starts the list conversion by converting the paired strings
### to integers                
    int_lst = [int(i) for i in pin_lst] 
    print(int_lst)
    n = len(int_lst)
        
### Takes an empty list and populates it with corresponding consonants    
    fin_con_lst = []
    for item in range(n):
        a = int_lst[item]   
        con_index = a // 5
        con_alpha = con_lst[con_index]
        fin_con_lst.append(con_alpha)
        
### Takes an empty list and populates it with corresponding vowels               
    fin_vow_lst = []
    for item in range(n):
        a = int_lst[item]    
        vow_index = a % 5
        vow_alpha = vow_lst[vow_index]
        fin_vow_lst.append(vow_alpha)

### Takes an empty list and populates it with the consonant-vowel pairs        
    final_word = []
    for item in range(n):
        pairs = fin_con_lst[item] + fin_vow_lst[item]
        final_word.append(pairs)  
        
### Returns a final string
    strg_lst = ''.join(str(e) for e in final_word)
    return strg_lst

### Converts an input string into a list of integers
def convert_word(word):
    CONSONANTS = "bcdfghjklmnpqrstvwyz" 
    VOWELS = "aeiou"
    con_lst = list(CONSONANTS)
    vow_lst = list(VOWELS) 
    
    u_word = str(word)
    length = len(u_word)
    con_pin = []
    vow_pin = []
    for char in range(0, length, 2):
        con = u_word[char] # this is a string of only consonants 
        con_index = con_lst.index(con) # this was the integer div result
        con_pin.append(con_index)
    
    for char in range(1, length, 2):
        vow = u_word[char]
        vow_index = vow_lst.index(vow)
        vow_pin.append(vow_index)

    fin_pin = []
    length2 = len(con_pin)
    for item in range(length2):

# using the formula a = qm + r
        q = con_pin[item]
        m = 5
        r = vow_pin[item]
        calc_pin = q * m + r
        fin_pin.append(calc_pin)
        print(fin_pin)
        
