def check_character(word, index):
   x=word[index]
   if len(word) < (index-1):
      return("unknown")
   elif x.isalpha():
      return("letter")
   elif x.isdigit():
      return("digit")
   elif x.isspace():
      return("whitespace")
   else:
      return("unknown")

if __name__ == '__main__': 
    print(check_character('happy birthday', 2))
    print(check_character('happy birthday', 5))
    print(check_character('happy birthday 2 you', 15))
    print(check_character('happy birthday!', 14))
