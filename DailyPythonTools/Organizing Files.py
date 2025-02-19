import os
import shutil

def organize_files(src_folder, dest_folder):
    """Organize files from src_folder to dest_folder based on file extension."""
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    
    for file_name in os.listdir(src_folder):
        file_path = os.path.join(src_folder, file_name)
        
        if os.path.isfile(file_path):
            ext = file_name.split('.')[-1]
            folder = os.path.join(dest_folder, ext)
            
            if not os.path.exists(folder):
                os.makedirs(folder)
            
            shutil.move(file_path, os.path.join(folder, file_name))

if __name__ == "__main__":
    src_folder = "path/to/your/folder"
    dest_folder = "path/to/organized/folder"
    organize_files(src_folder, dest_folder)
    print("Files organized successfully!")

