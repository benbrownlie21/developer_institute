from utils import unzip_with_7z

zip_file_path = 'congrats.7z' # keep as is
dest_path = '.' # keep as is

find_me = '' # 2 letters are missing!
secret_password = find_me + 'bcmpda' 

# WRITE YOUR CODE BELOW
# ----------------------------------------
alphabet = 'abcdefghijklmnopqrstuvxyz'

password_found = False

for i in alphabet:
    if password_found:
        break
    for j in alphabet:
        attempt = i + j + secret_password
        if unzip_with_7z(zip_file_path, dest_path, attempt):
            print("Success!")
            password_found = True
            break

