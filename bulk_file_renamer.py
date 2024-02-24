import os

def bulk_rename_files(folder_path, prefix):
    for index, filename in enumerate(os.listdir(folder_path)):
        # Split the file name and extension
        name, extension = os.path.splitext(filename)
        # Create the new file name
        new_name = f"{prefix}_{index}{extension}"
        # Rename the file
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_name))