import os

def create_md_file(folder_path):
    folder_name = os.path.basename(folder_path)
    md_filename = f"{folder_path}.md"
    content = f"""---
layout: directory
---

# {folder_name}
"""
    with open(md_filename, "w", encoding="utf-8") as md_file:
        md_file.write(content)

def traverse_directory(directory):
    for root, dirs, files in os.walk(directory):
        for dir_name in dirs:
            folder_path = os.path.join(root, dir_name)
            create_md_file(folder_path)

if __name__ == "__main__":
    starting_directory = "./"  # specify your starting directory here
    traverse_directory(starting_directory)
