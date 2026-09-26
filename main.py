import os
from pathlib import Path

while True:
    print("Options -")
    print("1. Create a Folder")
    print("2. Update the Folder")
    print("3. Delete the folder")
    print("4. Exit")

    print("-------------x-----------------x----------------x-----------x------------------x----------------x----------------")

    def creat_fol(name):
        try:
            path = Path(name)
            path.mkdir()

        except Exception as e:
            print(e)
    
    f = int(input("Enter the number: "))
    if f == 4:
        print("Thank you for using our product")
        break
    
    elif f == 1:
        name = input("Enter name of folder: ")
        creat_fol(name)


