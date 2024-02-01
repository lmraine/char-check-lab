def check_character(word, index):
   if len(word) < (index-1):
      return("unknown")
   elif word.isalpha(index)==true:
      return("letter")
   elif word.isdigit(index)==true:
      return("digit")
   elif word.isspace(index)==true:
      return("whitespace")
   else:
      return("unknown")

if __name__ == '__main__': 
    print(check_character('happy birthday', 2))
    print(check_character('happy birthday', 5))
    print(check_character('happy birthday 2 you', 15))
    print(check_character('happy birthday!', 14))
