import Encryptor


print("Welcome to the encryption application!\n\n")


check=True
while check==True:
    option = input("Do you want to encrypt or crypt a message?(Type 1 for encryption and 2 for decryption)\n")
    if option=='1':
        message=input("Give the message you want to encrypt:\n")
        key=input("Give the encryption key\n")
        encrypted_message=Encryptor.Encryptor(key,message)
        encrypted_message.encript()
        print("The encrypted message is:" + encrypted_message.message)
    elif option=='2':
        message = input("Give the message you want to decrypt:\n")
        key = input("Give the decryption key\n")
        decrypted_message = Encryptor.Encryptor(key, message)
        decrypted_message.decript()
        print("The decrypted message is: " + decrypted_message.message)
    else:
        print("Invalid user input!")

    cont=input("Do you want to continue using the application?(Y/N)")
    if cont=='N':
        check=False
