import argparse
import subprocess
import os
import re

def check_ctags():
    try:
        subprocess.run(['ctags', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def generate_tags(directory):
    subprocess.run(['ctags', '-R', '--c-kinds=+p', '--fields=+S', '--extra=+q', directory], check=True)

def filter_tags(directory,tags_file):
    temp_tags_path = os.path.join(directory,'temp_tags')
    tags_path = os.path.join(directory,tags_file)

    sed_command = r"cat {0} | sed -n 's/^.*\/^\(.*\)/\1/p'  | sed 's/\(.*\)\$.*/\1/' | sed 's/;$//' | uniq | sed '/int main(/d' | sed '/.*:/d' | sed 's/$/;/g' > {1}".format(tags_path, temp_tags_path)
    
    # Run the sed_command using subprocess
    subprocess.run(sed_command, shell=True, check=True)

    # Check if the file exists before trying to open it
    if os.path.exists(temp_tags_path):
        with open(temp_tags_path, 'r') as temp_tags_file:
            filtered_tags = temp_tags_file.read()
        return filtered_tags
    else:
        # Handle the case where the file doesn't exist
        print(f"Error: File {temp_tags_path} does not exist.")
        return None

    # Read the filtered tags from the temporary file
    with open('temp_tags', 'r') as temp_tags_file:
        filtered_tags = temp_tags_file.read()
    return filtered_tags


def create_header(header_file, filtered_tags):
    header_name = header_file.split('/')[-1]
    header_name =header_name.split('.')
    header_name= '_'.join(header_name)
    with open(header_file, 'w') as header:
        header.write(f'#ifndef {header_name.upper()}\n')
        header.write(f'#define {header_name.upper()}\n\n')
        header.write(filtered_tags)
        header.write('\n#endif\n')
def delete_files(tags, temp_tags):
    command = "rm {0} {1}".format(tags, temp_tags)
    subprocess.run(command, shell=True, check=True)
def check_directory(directory):
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return False
    return True

def check_header_file(header_file):
    if not header_file.endswith('.h'):
        print(f"Error: Invalid header file. It should have a '.h' extension.")
        return False
    return True
