import random
import string
import pyperclip

def password_generator():
    """ Creates a random generated password. """
    to_continue = True
    while to_continue:
        pass_lenght = int(input("Input the password length : "))
        result = "".join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*()-_+<>?",k = pass_lenght))
        print(result +'\n')
        pyperclip.copy(result)
        print('Password Copied To Clipboard!')
        
        another = input('Would you like to generate a new password? (Y/N)').lower()
        if another =='y':
            password_generator()
        else:
            to_continue = False 

password_generator()

