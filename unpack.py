import argparse
import os
import subprocess


def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"\033[0;32mFolder '{folder_name}' create success!")
    else:
        print(f"\033[0;31mFolder '{folder_name}' already exists!\033[0;32m")

def unpack(folder_name):
    cmd = f'corona-archiver.exe -u resource.car {folder_name}'
    subprocess.run(cmd, shell=True, check=True)
    
# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description="Buat folder berdasarkan argumen.")
#     parser.add_argument("folder_name", type=str, help="Nama folder yang akan dibuat.")
#     args = parser.parse_args()

#     create_folder(args.folder_name)
#     unpack(args.folder_name)
    
