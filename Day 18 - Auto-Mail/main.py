file1=open("Input/Letters/starting_letter.txt")
file2=open("Input/Names/invited_names.txt")


invitation_names=file2.read().split('\n')

invitation_body=file1.read().split('\n')
print(invitation_body)

for name in invitation_names:
    new_file = open('Output/ReadyToSend/' + name + '_invitation.txt', 'w')
    for line in invitation_body:
        new_string = line.replace("[name]", name)
        new_file.write(new_string)
        new_file.write('\n')

    new_file.close()

