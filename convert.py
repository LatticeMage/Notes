import os
import fnmatch

def remove_markdown_files_with_layout(directory):
    for root, dirs, files in os.walk(directory):
        for filename in fnmatch.filter(files, '*.md'):
            file_path = os.path.join(root, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                if any('layout: directory' in line for line in file):
                    os.remove(file_path)
                    print(f"Removed: {file_path}")

# Replace 'your_directory_path' with the path to the directory you want to search.
remove_markdown_files_with_layout('./')
