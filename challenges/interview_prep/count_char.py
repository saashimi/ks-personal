def count_letter(str_):
    lst_str = list(str_)
    set_str = set(str_)
    fin_lst = []
    for item in set_str:
        num_char = str_.count(item)
        tup = (item, num_char)
        fin_lst.append(tup)
    fin_lst.sort(key = lambda x: x[1])
    print(fin_lst)
    return fin_lst

def main():
    str_ = input("Enter a string. >> ")
    count_letter(str_)

assert count_letter("a") == [('a', 1)]
assert count_letter("abs") == [('a', 1), ('b', 1), ('s', 1)]
assert count_letter("tool") == [('o', 2), ('l', 1), ('t', 1)]

if __name__ == "__main__":
    main()