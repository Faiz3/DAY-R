import unpack
import pack
import decompile
import os


run = True
folder_name = 'resource'
folder_path = "."

def menu():
    os.system('cls')
    print('''
\033[0;32m ___  ___  _ _      \033[0;31m ___ 
\033[0;32m| . \| . || | | ___ \033[0;31m| . \\
\033[0;32m| | ||   |\   /|___|\033[0;31m|   /
\033[0;32m|___/|_|_| |_|      \033[0;31m|_\_\\
                         
    \033[0;32m1. unpack
    2. decompile-all
    3. pack
    \033[0;31m0. exit\033[0m
    ''')

while run:
    menu()
    select_menu = int(input('Menu: '))
    if select_menu == 1:
        unpack.create_folder(folder_name)
        unpack.unpack(folder_name)
    elif select_menu == 2:
        print('process...')
        decompile.scan_and_process_files(folder_path)
    elif select_menu == 3:
        print('\033[0;32m')
        pack.pack(folder_name)
    elif select_menu == 0:
        run = False
    input('\033[0mEnter...')
    os.system('cls')
