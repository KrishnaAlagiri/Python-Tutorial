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
import re,os

def print_items ():
    mydir = input("\rEnter Directory: ")
    paths = os.listdir(mydir)
    if(mydir[len(mydir)-1]!="\\"):
        mydir+="\\"
    for i in paths:
        print(mydir+i)


def print_items_no_dir ():
    paths = []
    mydir = input("\rEnter Directory: ")
    for (dirpath, dirnames, filenames) in os.walk(mydir):
        dir = dirpath+"\\"
        paths.extend(filenames)
        break
    for i in paths:
        print(dir+i)

def print_pics ():
    paths = []
    mydir = input("\rEnter Directory: ")
    for (dirpath, dirnames, filenames) in os.walk(mydir):
        dir = dirpath+"\\"
        paths.extend(filenames)
        break
    for i in paths:
        if (i.endswith(".png") or i.endswith(".jpg")):
            print(dir+i)

def print_no_spaces ():
    string = input("\rEnter string: ")
    print("Count of Spaces: ",string.count(' '))

def remove_vowels ():
    string = input("\rEnter string: ")
    string = re.sub(r'[AEIOU]', '', string, flags=re.IGNORECASE)
    print(string)


def print_less_4 ():
    string = input("\rEnter string: ")
    for word in string:
        if(len(word) > 4):
            print(word)

def print_length_of_each_word ():
    sentence = input("\rEnter sentence: ")
    for word in sentence:
        print(word,"\t",len(word))
