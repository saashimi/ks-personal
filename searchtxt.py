"""Searches for a list in a file """

"""Imports a text file """
def open_txt():
    filename = input("input filename ")
    file = open(filename, 'r')
    print("Opened " + filename + ".")

def count_commits():
    add_lst = []
    for line in file:
        if "From" in line:
            a = line.split()
            if len(a) > 2:
                add_lst.append(a[1])
    
    num_lst = []
    for item in range(len(add_lst)):
        email = add_lst[item]
        commit = add_lst.count(add_lst[item])
        num = commit, email
        num_lst.append(num)
    num_lst.sort(reverse=True)

    print(num_lst[0])
    filename.close()

__name__ == "__main__"
