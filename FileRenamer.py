import os

print("-" * 25)
print("Current Working Directory (CWD): " + os.getcwd())
print()
print("Files in CWD: " + str(os.listdir()))
print('-' * 25)

print("Please specify the full path of the file/folder you wish to rename")
file_to_rename = input("Path to file being renamed: ")
new_file_name = input("What would you like to rename it to?: ")

os.rename(file_to_rename, new_file_name)
print("Renaming Complete")



### TODO: Get to work with Relative Filepath... currently only works if the full file path is
###       given manually, even when dragging the file to terminal and it provides the full path.

### TODO: check that the path to the file given is valid (does file actually exist?)

### TODO: why doesn't this work when you drag file to terminal, that provides full path,
###       yet it throws a FileNotFound error.
