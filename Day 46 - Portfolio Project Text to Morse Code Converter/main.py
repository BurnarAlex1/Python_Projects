morse_dict={'A':'. -','B':'- . . .','C':'. .  .','D':'- . .'
    ,'E':'.','F':'. - .','G':'- - .','H':'. . . .','I':'. .'
    ,'J':'- . - .','K':'- . -','L':'--','M':'- -','N':'- .'
    ,'O':'.  .','P':'. . . . .','Q':'. . - .','R':'.  . .','S':'. . .','T':'-'
    ,'U':'. . -','V':'. . . -','W':'. - -','X':'. - . .','Y':'. .  . .','Z':'. . .  .'}

print("Text Converter to Morse Code")
message=input("Give the message you want converted: ")
for letter in message:
    new_letter=morse_dict[letter.upper()]
    print(new_letter)
