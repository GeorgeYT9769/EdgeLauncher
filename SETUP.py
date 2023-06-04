import os

print("Downloading packages...\n   ")
os.system("py -m pip install -r requirements.txt")
exit = input("\nIf you don't see any error, that means the installation was sucessful. \nPress Enter to exit.")
