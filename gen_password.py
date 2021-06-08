import os
import random
from string import ascii_uppercase, ascii_lowercase, punctuation

#MACROS
FILE_DIR = './files'
RETRY = 'RETRY'
SPECIAL_CHARS_ENABLED = 's_c_e'
FILE_NAME_INPUT = 'f_n'

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

def verify_input(input_type, file_name=''):
    
    if input_type == SPECIAL_CHARS_ENABLED:
        answer = ' '

        while (answer.upper() != 'N') and (answer.upper() != 'S'):
            answer = input("usar caracteres especiales (s/n): ")
            if (answer.upper() != 'N') and (answer.upper() != 'S'):
                print('Respuesta no valida, intente de nuevo')
        
        if answer.upper() == 'S':
            return True
        else:
            return False
    
    elif input_type == FILE_NAME_INPUT:
        file_name = file_name
        change_file = ''
        if  (file_name+'.txt') in os.listdir(FILE_DIR):
            while (change_file.upper() != 'N') and (change_file.upper() != 'S'):
                change_file = input('El nombre de archivo ya existe, desea reemplazarlo? (s/n): ')
                if (change_file.upper() != 'N') and (change_file.upper() != 'S'):
                    print('Respuesta no valida, intente de nuevo')
            
            if change_file.upper() == 'S':
                return file_name
            else:
                return RETRY
        else:
            return file_name

def create_file(file_name, password):
    with open(f'{FILE_DIR}/{file_name}.txt','w') as file:
        file.write(password + '\n')

def main():
    if not 'files' in os.listdir():
        os.mkdir(FILE_DIR)

    while True:
        file_name = input("Nombre : ")
        file_name = verify_input(FILE_NAME_INPUT,file_name=file_name)
        if file_name != RETRY:
            break
        
    length = int(input("ingresar largo de la contraseña: "))
    special_chars_enabled = verify_input(SPECIAL_CHARS_ENABLED)
    
    '''
    if special_chars_enabled == 's':
        special_chars_enabled = True
    else:
        special_chars_enabled = False
    '''    
    password = generate_password(length, special_chars_enabled)
    print(f'''new password created: {password}, 
    saving it in {file_name}.txt''')

    create_file(file_name, password)


if __name__ == '__main__':
    main()
