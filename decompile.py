import os
import subprocess
import sys


def print_progress_bar(iteration, total, length=50):
    percent = 100 * (iteration / float(total))
    filled_length = int(length * iteration // total)
    bar = '\033[0;32m=' * filled_length + '\033[0;31m-\033[0m' * (length - filled_length)
    # sys.stdout.write(f'\r[{bar}] {percent:.1f}%')
    # sys.stdout.flush()
    spinner = '|/-\\'
    for i in range(length):
        print(f'\r\033[K[{bar}]{percent:.1f}%\nloading {spinner[i%len(spinner)]}\033[F', end='', flush=True)

def scan_and_process_files(folder_path):
    if not os.path.exists(folder_path):
        print(f"Folder {folder_path} does not exist")
        return

    jar_files = []
    lu_files = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.jar'):
                full_path = os.path.join(root, file)
                jar_files.append(full_path)
            elif file.endswith('.lu'):
                full_path = os.path.join(root, file)
                lu_files.append(full_path)

    if not jar_files:
        print("No JAR files found")
        return

    if not lu_files:
        print("No .lu files found in resources folder")
        return

    total_tasks = len(jar_files) * len(lu_files)
    completed_tasks = 0

    for jar_path in jar_files:
        jar_name = os.path.basename(jar_path)
        jar_folder = os.path.splitext(jar_name)[0]
        output_dir = os.path.join(folder_path, jar_folder)
        os.makedirs(output_dir, exist_ok=True)

        for lu_path in lu_files:
            lu_name = os.path.basename(lu_path)
            output_file = os.path.join(output_dir, f"{lu_name}a")
            cmd = f'java -jar "{jar_path}" "./resource/{lu_name}" > "{output_file}"'

            try:
                subprocess.run(cmd, shell=True, check=True)
                completed_tasks += 1
                print_progress_bar(completed_tasks, total_tasks)
            except subprocess.CalledProcessError as e:
                print(f"\nError processing {lu_name} with {jar_name}: {e}")

    print("\n\033[0;32mProcessing completed.\033[0m")