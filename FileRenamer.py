import os
import os.path

print("-" * 60)
print("Current Working Directory (CWD): " + os.getcwd())
print()
print("Files in CWD: " + str(os.listdir()))
print('-' * 60)

print("Please specify the file you wish to rename (listed above)")
file_to_rename = input("File to rename: ")

### This check works, put absolute file paths conflict with while loop below
# if os.path.isabs(file_to_rename) == True:
#     print("absolute")
# else:
#     print("relative")


while file_to_rename not in os.listdir():
    print("File not in FileRenamer directory!")
    file_to_rename = input("File to rename: ")

new_file_name = input("What would you like to rename it to?: ")

os.rename(file_to_rename, new_file_name)
print("Renaming Complete")




### TODO: prevent user from renaming the python file
### TODO: and if else clause to allow absolute and relative file paths (if it has a /?)
### TODO: why doesn't this work when you drag file to terminal, that provides full path,
###       yet it throws a FileNotFound error.

### TODO: if user doesn't give file extension, use the original files extension
