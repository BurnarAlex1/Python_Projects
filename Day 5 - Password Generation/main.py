import random


letters =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','v','w','x','y','z']
symbols =[',','.',']','[','#','%','^','&','*','@','!',')','(']
digits =['1','2','3','4','5','6','7','8','9','0']

print('Password Generator\n')
nr_letters=int(input('Give the number of letters you want in your password\n'))
nr_symbols=int(input('Give the number of symbols you want in your password\n'))
nr_digits=int(input('Give the number of digits you want in your password\n'))

password=[]

while nr_letters>0:
    password.append(letters[random.randint(0,len(letters)-1)])
    nr_letters=nr_letters-1

while nr_symbols>0:
    password.append(symbols[random.randint(0,len(symbols)-1)])
    nr_symbols=nr_symbols-1

while nr_digits>0:
    password.append(digits[random.randint(0,len(digits)-1)])
    nr_digits=nr_digits-1

random.shuffle(password)
print("Your generated password: ")
passw=''
for character in password:
    passw=passw+character
print(passw)



