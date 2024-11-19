from cryptography.fernet import Fernet
import tkinter as tk
import os
import imghdr

# TODO:
# - ADD a way to encrypt/decrypt entire directories.
# - ADD a way to manually select key file/path to create key file in.

if os.path.exists('file-encrypter.key') == False: # If file-encrypter.key file does not exist, create it.
    open('file-encrypter.key', 'x')

with open('file-encrypter.key', 'rb') as filekey:
    file_size = os.path.getsize('file-encrypter.key') 
    if file_size < 10: # If the file is empty, generate a key. Used for first time use.
        with open('file-encrypter.key', 'wb') as filekey:
            key = Fernet.generate_key()
            filekey.write(key)
    else:
        key = filekey.read() # Read the key from file-encrypter.key file.

fernet = Fernet(key)

# Used to encrypt images.
def encrypt_image(img):
    with open(img, 'rb') as file:
        file_data = file.read()

    encrypted_data = fernet.encrypt(file_data)

    with open(img, 'wb') as file:
        file.write(encrypted_data)

# Used to encrypt files.
def encrypt_file(filename):
    if imghdr.what(filename): # If the file is an image, encrypt it as an image.
        encrypt_image(filename)
    else:
        with open(filename, 'r') as file: # Read file contents.
            file_data = file.read()

        encrypted_data = fernet.encrypt(file_data.encode()) # Encrypt file contents.

        with open(filename, 'w') as file: # Write encrypted data to file.
            file.write(encrypted_data.decode())

# Used to decrypt files.
def decrypt_file(filename):
    with open(filename, 'rb') as file: # Read file contents.
        file_data = file.read()

    decrypted_data = fernet.decrypt(file_data)

    with open(filename, 'wb') as file: # Write decrypted data to file.
        file.write(decrypted_data)

# GUI
app = tk.Tk()
app.title("File Encrypter")
app.geometry("300x80")
app.resizable(False, False)

frame = tk.Frame(app)
frame.pack()

filepath_label = tk.Label(frame, text="Enter filepath:")
filepath_label.grid(row=0, column=0, pady=10)
filepath = tk.Entry(frame)
filepath.grid(row=0, column=1)

encrypt_button = tk.Button(frame, text="Encrypt", command=lambda: encrypt_file(filepath.get()))
encrypt_button.grid(row=1, column=0, pady=0)

decrypt_button = tk.Button(frame, text="Decrypt", command=lambda: decrypt_file(filepath.get()))
decrypt_button.grid(row=1, column=1)

app.mainloop()