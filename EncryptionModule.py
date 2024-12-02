from cryptography.fernet import Fernet
import os, filetype

# Used to select key file.
def select_key_file(keyfile):
    if os.path.exists(keyfile) == False: # If file-encrypter.key file does not exist, create it.
        with open(keyfile, 'wb') as filekey:
            key = Fernet.generate_key()
            filekey.write(key)
    
    with open(keyfile, 'rb') as filekey:
        key = filekey.read() # Read the key from file-encrypter.key file.
    
    return Fernet(key)

# Used to encrypt images.
def encrypt_image(img, fernet_key):
    with open(img, 'rb') as file:
        file_data = file.read()

    encrypted_data = fernet_key.encrypt(file_data)

    with open(img, 'wb') as file:
        file.write(encrypted_data)

# Used to encrypt files.
def encrypt_file(filename, fernet_key):
    kind = filetype.guess(filename)
    if kind and kind.mime.startswith('image/'): # If the file is an image, encrypt it as an image.
        encrypt_image(filename, fernet_key)
    
    else:
        with open(filename, 'r') as file: # Read file contents.
            file_data = file.read()

        encrypted_data = fernet_key.encrypt(file_data.encode()) # Encrypt file contents.

        with open(filename, 'w') as file: # Write encrypted data to file.
            file.write(encrypted_data.decode())

# Used to decrypt files.
def decrypt_file(filename, fernet_key):
    with open(filename, 'rb') as file: # Read file contents.
        file_data = file.read()

    decrypted_data = fernet_key.decrypt(file_data)

    with open(filename, 'wb') as file: # Write decrypted data to file.
        file.write(decrypted_data)

