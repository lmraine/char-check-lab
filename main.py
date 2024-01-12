#Remove pass and complete the code
def check_character(word, index):
   pass

if __name__ == '__main__': 
    print(check_character('happy birthday', 2))
    print(check_character('happy birthday', 5))
    print(check_character('happy birthday 2 you', 15))
    print(check_character('happy birthday!', 14))

#Solution
'''def check_character(word, index):
    c = word[index]
    if c.isalnum() and not c.isdigit():
        return "letter"
    elif c.isdigit():
        return "digit"
    elif c.isspace():
        return "white space"
    else:
        return "unknown"'''