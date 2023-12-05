class Encryptor:

    def __init__(self,key,message):
        self.encryption_key=int(key)
        self.message=message

    def encript(self):
        cripted_message=''
        for letter in self.message:
            cripted_message=cripted_message+chr(ord(letter)+self.encryption_key)

        self.message=cripted_message

    def decript(self):
        decripted_message=''
        for letter in self.message:
            decripted_message=decripted_message+chr(ord(letter)-self.encryption_key)

        self.message=decripted_message


