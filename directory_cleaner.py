import os
import shutil

def organize_folder(folder_path):
    # Mapping file extensions to folder names
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
        'Scripts': ['.py', '.js', '.cpp'],
        'Compressed': ['.zip', '.tar', '.rar']
    }

    for filename in os.listdir(folder_path):
        ext = os.path.splitext(filename)[1].lower()
        
        for folder, extensions in file_types.items():
            if ext in extensions:
                target_folder = os.path.join(folder_path, folder)
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(os.path.join(folder_path, filename), 
                            os.path.join(target_folder, filename))
                print(f"Moved: {filename} -> {folder}")

# Usage
# organize_folder('/path/to/your/downloads')
