import random

words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

class guessword:

    def __init__(self):
        self.word=''
        self.letters=[]
        self.hidden_letters=[]


    def choose_word(self):
        self.word = words[random.randint(0, len(words) - 1)]
        self.letters=list(self.word)
        for letter in self.letters:
            self.hidden_letters.append('_')


    def check_letter(self,checked_letter):
        check_found=False
        while True:
            try:
                found_letter=self.letters.index(checked_letter)
            except:
                return check_found
            else:
                check_found=True
                found_letter=self.letters.index(checked_letter)
                self.hidden_letters[found_letter]=checked_letter
                self.letters[found_letter]='-'







