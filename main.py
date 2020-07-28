import os
import shutil
import smtplib


#* The function to get the file location
def get_file_location():
    #? Where is the file
    fileLocation = str(input("Enter the location of the file: "))
    #? What is the file name
    fileNameToBeChanged = str(input("Enter the file name: "))

    #* Going to that location
    os.chdir(fileLocation)
    ActualFileLocation = os.path.join(fileLocation, fileNameToBeChanged)
    if os.path.isfile(ActualFileLocation):
        what_want_to_do_with_file(fileLocation, fileNameToBeChanged)
    else:
        print("That file location is incorrect")


#* The function for what to do with the file
def what_want_to_do_with_file(filel, filen):
    allThingsCanDo = [
        "1. Rename",
        "2. Make all uppercase",
        "3. Make all lowercase",
        "4. Remove underscores to capitals",
        "5. Relocate",
    ]
    print()
    #* Printing the options
    for thing in allThingsCanDo:
        print(thing)
    #? What do you want to do
    print()
    wantsToDo = int(input("Enter the number before the operation you want to do: "))
    print()

    #* All the cases
    if wantsToDo == 1:
        rename_file(filel, filen)
    elif wantsToDo == 2:
        make_all_uppercase(filel, filen)
    elif wantsToDo == 3:
        make_all_lowercase(filel, filen)
    elif wantsToDo == 4:
        remove_underscores(filel, filen)
    elif wantsToDo == 5:
        relocate_file(filel, filen)


#* The function to rename
def rename_file(filelocation, currentname):
    #? What is the rename
    renamedName = str(input("Wahat is the name that you want the file to be chnged to? "))

    #* Renaming the file
    os.rename(os.path.join(filelocation, currentname), os.path.join(filelocation, renamedName))
    #* Printing it out
    print()
    print(f"{currentname} has been renamed to {renamedName}")
    print()


#* The function to make all uppercase
def make_all_uppercase(filelocation, currentname):
    #* Renaming the file
    os.rename(os.path.join(filelocation, currentname), os.path.join(filelocation, currentname.upper()))
    #* Printing it out
    print()
    print(f"{currentname} has been renamed to {currentname.upper()}")
    print()


#* The function to make all lowercase
def make_all_lowercase(filelocation, currentname):
    #* Renaming the file
    os.rename(os.path.join(filelocation, currentname), os.path.join(filelocation, currentname.lower()))
    #* Printing it out
    print()
    print(f"{currentname} has been renamed to {currentname.lower()}")
    print()


#* The function to remove underscore
def remove_underscores(filelocation, currentname):
    #? Is there an undersocre in the name
    for x in currentname:
        if x == "_":
            charAfterUnder = currentname[(currentname.index(x) + 1)]
            currentnameUpdated = currentname.replace("_", charAfterUnder.upper()).replace(currentname[(currentname.index(x) + 1)], "")
            os.rename(os.path.join(filelocation, currentname), os.path.join(filelocation, currentnameUpdated))
    
    #* Printing out the result
    print(f"{currentname} has been renamed to {currentnameUpdated}")


#* The function to relocate
def relocate_file(filelocation, currentname):
    newLocationWants = str(input("Enter the new location of the file: "))
    if os.path.isdir(newLocationWants):
        os.chdir(newLocationWants)
        shutil.move(os.path.join(filelocation, currentname), newLocationWants)
        print("File has been moved to the new location!")
    else:
        print("Not a valid location!")


#* Calling the function
get_file_location()