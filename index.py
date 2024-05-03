import hashlib
from cryptography.fernet import Fernet


#This will store your input.
string_to_hash = input('What do you want to hash and encrypt? ')

def encryptdecrypt(string):
    
    #key needs to be generated.
    key = Fernet.generate_key()

    cipher = Fernet(key)

    #This encrypts the string that was stored.
    #Earlier.
    encrypted_message = cipher.encrypt(string.encode('utf-8'))

    #This is going to decrypt the string.
    decrypt_message = cipher.decrypt(encrypted_message)


    return encrypted_message, decrypt_message


#Next is the hash. Let's create the function now.

def hash_string(string):

    hasher = hashlib.sha256()

    hasher.update(string.encode('utf-8'))
    hashed_string = hasher.hexdigest()

    return hashed_string


the_hashed_string = hash_string(string_to_hash)
encryptedMessage, decrypted_message = encryptdecrypt(string_to_hash)

print("This is the encrypted message: ", encryptedMessage)
print("Here is the hash as well: ", the_hashed_string)
print("Decrypted message: ", decrypted_message.decode())

#Let's see what happens.