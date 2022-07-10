# Importing OS Module to edit file names
import os


def main():
    folder = "IMAGES"
    # os.listdir(folder) to list directory files
    imagemani = input("Enter the prefix (NO SPACES IF YOU WANT TO USE AS LINK: ")
    for count, filename in enumerate(os.listdir(folder)):
        # Edit the contents of f string to if you want to remove or
        # take a specific parts of strings, string manipulations can be used


        destination = f"{imagemani}{filename[5:]}"
        print(destination) # This prints edited file names
        src = f"{folder}/{filename}"  # folder name/filename, if .py file is outside folder
        destination = f"{folder}/{destination}"

        # rename() function will
        # rename all the files
        os.rename(src, destination)


if __name__ == '__main__':
    # Calling main() function
    main()