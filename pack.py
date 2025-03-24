import subprocess
# import argparse

folder_name = 'resource'
def pack(folder_name):
    cmd = f'corona-archiver.exe -p {folder_name} {folder_name}.car'
    subprocess.run(cmd, shell=True, check=True)

# if __name__=="__main__":
    # parser = argparse.ArgumentParser(description="Input folder name for packing")
    # parser.add_argument("folder_name", type=str, help="Folder name want to packing")
    # args = parser.parse_args()
    
    # pack(folder_name)