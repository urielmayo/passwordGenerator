import random
from string import ascii_uppercase, ascii_lowercase, punctuation

def generate_password(length, special_chars = False):
    upper_letters = list(ascii_uppercase)
    lower_letters = list(ascii_lowercase)
    special_characters = list(punctuation)
    numbers = [str(number) for number in range(10)]


    total_characters = upper_letters + lower_letters + numbers
    
    if special_chars:
        total_characters += special_characters

    password = [random.choice(total_characters) for i in range (length)]
    password = "".join(password)
    
    return password


def main():
    length = int(input("ingresar largo de la contraseña: "))
    special_chars_enabled = input("usar caracteres especiales (s/n): ")
    
    if special_chars_enabled == 's':
        special_chars_enabled = True
    else:
        special_chars_enabled = False
        
    password = generate_password(length, special_chars_enabled)
    print(password)


if __name__ == '__main__':
    main()