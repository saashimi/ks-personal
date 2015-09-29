def break_string(string_input):
    lst = []
    for char in string_input:
        lst.append(char)
    return lst

def string_count(lst_input):
    count_lst = []
    for char in lst_input:
        counts = lst_input.count(char)
        count_lst.append(counts)
    count_lst.sort(reverse = True)
    return count_lst

def check_unique(count_input):
    for item in count_input:
        if item > 1:  
            return False
        else:      
            return True

def unique_chars(string):
    str_to_lst = break_string(string)
    #print(str_to_lst)
    counted = string_count(str_to_lst)
    #print(counted)
    #print(check_unique(counted))
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
