import os
import shutil

def organize_desktop():
    # Path to the desktop
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    # Dictionary to store folders for each file extension
    folders = {
        "Documents": ["doc", "docx", "txt", "pdf", "ppt", "pptx", "xls", "xlsx"],
        "Images": ["png", "jpg", "jpeg", "gif", "bmp"],
        "ZipArchives": ["zip", "rar", "7z", "tar", "gz"]
        # Add more categories if needed
    }

    # Create folders if they don't exist
    for folder in folders.keys():
        folder_path = os.path.join(desktop_path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Move files to appropriate folders based on their extensions
    for filename in os.listdir(desktop_path):
        if filename != "organize_files.py":  # Exclude this script
            file_path = os.path.join(desktop_path, filename)
            if os.path.isfile(file_path):
                file_extension = filename.split(".")[-1].lower()
                for folder, extensions in folders.items():
                    if file_extension in extensions:
                        destination_folder = os.path.join(desktop_path, folder)
                        shutil.move(file_path, destination_folder)
                        print(f"Moved {filename} to {destination_folder}")
                        break

if __name__ == "__main__":
    organize_desktop()
