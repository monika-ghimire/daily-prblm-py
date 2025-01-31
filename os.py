import os

# Check if a file or directory exists
path = "/"
if os.path.exists(path):
    print(f"{path} exists!")

    print(os.listdir(path))
else:
    print(f"{path} does not exist.")
