"""
  List Comprehension Assignment
================================
Write a program list_comprehension_assignment.py with separate functions for:
    * printing a list of the full path to items in a directory
    * printing a list of the full path to items in a directory (excluding directories)
    * printing the list of all .jpg and .png files in a directory
    * printing the number of spaces in a string
    * removing vowels from a string and printing it
    * printing all of the words in a string that have less than 4 letters
    * printing length of each word in a sentence.
"""
import re,os,sys

def print_items ():
    print("\rPrint Items with Folders: ")
    mydir = input("\rEnter Directory: ")
    try:
        paths = os.listdir(mydir)
        if(mydir[len(mydir)-1]!="\\"):
            mydir+="\\"
        for i in paths:
            print(mydir+i)
    except:
        print("Directory not Found (or) inaccessabile")

def print_items_no_dir ():
    print("Print Items without Folders")
    paths = []
    mydir = input("\rEnter Directory: ")
    try:
        for (dirpath, dirnames, filenames) in os.walk(mydir):
            dir = dirpath+"\\"
            paths.extend(filenames)
            break
        for i in paths:
            print(dir+i)
    except:
        print("Directory not Found (or) inaccessabile")

def print_pics ():
    print("Print all .png and .jpg files")
    paths = []
    mydir = input("\rEnter Directory: ")
    try:
        for (dirpath, dirnames, filenames) in os.walk(mydir):
            dir = dirpath+"\\"
            paths.extend(filenames)
            break
        for i in paths:
            if (i.endswith(".png") or i.endswith(".jpg")):
                print(dir+i)
    except:
        print("Directory not Found (or) inaccessabile")

def print_no_spaces ():
    print("Count of number of spaces in a string")
    string = input("\rEnter string: ")
    print("Count of Spaces: ",string.count(' '))

def remove_vowels ():
    print("Remove Vowels and Print the String")
    string = input("\rEnter string: ")
    string = re.sub(r'[AEIOU]', '', string, flags=re.IGNORECASE)
    print(string)

def print_less_4 ():
    print("Print Less 4")
    string = input("\rEnter string: ")
    for word in string.split():
        if(len(word) < 4):
            print(word)

def print_len_of_word ():
    print("Print Length of Each Word")
    sentence = input("\rEnter sentence: ")
    for word in sentence.split():
        print(word,"\t",len(word))

def menu():
    print("\r  MENU\n========")
    print("1. Print Items with Folders")
    print("2. Print Items without Folders")
    print("3. Print all .png and .jpg files")
    print("4. Remove Vowels and Print the String")
    print("5. Print Less 4")
    print("6. Count of number of spaces in a string")
    print("7. Print Length of Each Word")
    print("8. Exit")
    argument = input("\nEnter Choice: ")
    print()
    if argument == '1':
        print_items()
    elif argument == '2':
        print_items_no_dir()
    elif argument == '3':
        print_pics()
    elif argument == '4':
        remove_vowels()
    elif argument == '5':
        print_less_4()
    elif argument == '6':
        print_no_spaces()
    elif argument == '7':
        print_len_of_word()
    elif argument == '8':
        sys.exit()
    else:
        print("Invalid Input")

# Driver program
if __name__ == '__main__':
  menu()
