import secrets
import string

def password_gen(password_len = 15):
    letters = string.ascii_letters
    numbers = string.digits
    special_characters = string.punctuation
    
    characterchoices = letters + numbers + special_characters
    password = ''
    passwordstrong = False
    
    while not passwordstrong:
        password = ''
        for i in range(password_len):
            password += ''.join(secrets.choice(characterchoices))
            
        if (any(char in special_characters for char in password) and sum(char in numbers for char in password) >= 5):
            passwordstrong = True
            
    return password

if __name__ == '__main__':
    password_len = int(input('How long would you like your password to be? '))
    print(password_gen(password_len))