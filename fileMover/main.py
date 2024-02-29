import os
import shutil

def move_files_to_folders(downloads_folder):
    downloads_path = os.path.expanduser(downloads_folder)

    program_folder = os.path.join(downloads_path, "Programs")
    os.makedirs(program_folder, exist_ok=True)

    university_folder = os.path.join(downloads_path, "University")
    os.makedirs(university_folder, exist_ok=True)

    application_extensions = [".exe", ".dmg", ".app", ".msi"]

    pdf_extensions = [".pdf"]

    for filename in os.listdir(downloads_path):
        if os.path.isfile(os.path.join(downloads_path, filename)):
            _, file_extension = os.path.splitext(filename)
            if file_extension.lower() in application_extensions:
                shutil.move(os.path.join(downloads_path, filename), program_folder)
            elif file_extension.lower() in pdf_extensions:
                shutil.move(os.path.join(downloads_path, filename), university_folder)

if __name__ == "__main__":
    downloads_folder_path = "C:/Users/talha/Downloads"

    move_files_to_folders(downloads_folder_path)
