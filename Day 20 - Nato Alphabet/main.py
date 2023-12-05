import csv



student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

nato_data=open('nato_phonetic_alphabet.csv')
#Looping through dictionaries:
old_data=nato_data.readlines()
new_data=[]
for i in range(0,len(old_data)):
    new_data.append(old_data[i].replace('\n',''))

values=[]
dict={}
for line in new_data:
    values=line.split(',')
    dict[values[0]]=values[1]


user_word=input("Give the word you want to transmit: ")
for letter in user_word:
    print(dict[letter])

