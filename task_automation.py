import os
import shutil

def organize_files(directory):
    # Get all files in the directory
    files = os.listdir(directory)

    # Create subdirectories for each file type
    for file in files:
        if os.path.isfile(os.path.join(directory, file)):
            file_extension = file.split('.')[-1]
            new_directory = os.path.join(directory, file_extension)

            # Create the subdirectory if it doesn't exist
            if not os.path.exists(new_directory):
                os.makedirs(new_directory)

            # Move the file to the appropriate subdirectory
            shutil.move(os.path.join(directory, file), os.path.join(new_directory, file))

    print("File organization complete.")

# Example usage you can give absolute path of the directory that you want to automated
organize_files(r'C:\Users\moham\Desktop\mame')