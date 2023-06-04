import os

def print_folder_hierarchy(folder_path, indent=''):
    folder_name = os.path.basename(folder_path)
    if folder_name == '.git':
        return
    
    print(indent + folder_name + '/')
    indent += '    '

    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            print_folder_hierarchy(item_path, indent)

# Prompt the user for the folder path
folder_path = input("Enter the folder path: ")

# Check if the provided path is a directory
if not os.path.isdir(folder_path):
    print("Invalid folder path.")
else:
    # Print the folder hierarchy
    print_folder_hierarchy(folder_path)