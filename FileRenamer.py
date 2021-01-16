import os
import os.path

print("-" * 60)
print("Current Working Directory (CWD): " + os.getcwd())
print()
print("Files in CWD: " + str(os.listdir()))
print('-' * 60)

print("Please specify the file you wish to rename (listed above)")
file_to_rename = input("File to rename: ")

while os.path.exists(file_to_rename) == False:
    print("That file doesn't exist, please enter a valid file path")
    file_to_rename = input("File to rename: ")

new_file_name = input("What would you like to rename it to?: ")

os.rename(file_to_rename, new_file_name)
print("Renaming Complete")




### TODO: prevent user from renaming the python file
### TODO: if user doesn't give file extension, use the original files extension
### TODO: files in subfolders get moved to main folder after renaming

### TODO: why doesn't this work when you drag file to terminal, that provides full path,
###       yet it throws a FileNotFound error.
