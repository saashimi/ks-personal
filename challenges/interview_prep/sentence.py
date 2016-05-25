def str_reverse(sentence):
    str_lst = sentence.split(" ")
    str_lst = str_lst[::-1]
    fin_sentence = ""
    for item in str_lst:
        sentence += item + " "
    print(sentence)
    return(sentence)

def main():
    sentence = input()
    str_reverse(sentence)

assert str_reverse("This is my sentence.") == "sentence. my is This "

if __name__ == "__main__":
    main()
