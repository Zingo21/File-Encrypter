from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import filedialog
import os
import filetype

# TODO:
# - ADD folder encryption/decryption functionality.
# - ADD a way to encrypt/decrypt entire directories.
# - ADD a way to manually select key file/path to create key file in.
# - FIX bug where the select file button crashed the whole program. (Might be OS X specific)

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
    kind = filetype.guess(filename)
    if kind and kind.mime.startswith('image/'): # If the file is an image, encrypt it as an image.
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

def select_file():
    filepath.delete(0, tk.END) # Clear text field.

    if filepath.get() == "":
        filepath_select = tk.filedialog.askopenfilename(initialdir=".", title="Select file", filetypes=(("all files", "*.*"), ("image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp;*.tiff;*.webp"), ("text files", "*.txt;*.docx;*.doc;*.pdf;*.rtf;*.odt;*.html;*.xml;*.csv;*.json;*.log;*.md;*.tex;*.yaml;*.yml;*.ini;*.cfg;*.conf;*.properties;*.env;*.sh;*.bat;*.cmd;*.ps1;*.psm1;*.psd1;*.ps1xml;*.pssc;*.psc1")))
    else:
        filepath_select = filepath.get()
        
    return filepath_select

# GUI
app = tk.Tk()
app.title("File Encrypter")
app.geometry("400x100")
app.resizable(False, False)

label_frame = tk.Frame(app)
label_frame.pack()
filepath_label = tk.Label(label_frame, text="Enter filepath:")
filepath_label.grid(row=0, column=0, pady=10)

filepath = tk.Entry(label_frame)
filepath.grid(row=0, column=1)

select_button = tk.Button(label_frame, text="Select file", command=lambda: filepath.insert(0, select_file()))
select_button.grid(row=0, column=2)

#key_select = tk.filedialog.askopenfilename(initialdir=".", title="Select key file", filetypes=(("key files", "*.key"), ("all files", "*.*")))

encrypt_decrypt_frame = tk.Frame(label_frame)
encrypt_decrypt_frame.grid(row=1, column=1, pady=10)

encrypt_button = tk.Button(encrypt_decrypt_frame, text="Encrypt", command=lambda: encrypt_file(filepath.get()))
encrypt_button.grid(row=1, column=0, pady=0)

decrypt_button = tk.Button(encrypt_decrypt_frame, text="Decrypt", command=lambda: decrypt_file(filepath.get()))
decrypt_button.grid(row=1, column=1)

app.mainloop()