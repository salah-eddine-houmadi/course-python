#problem

with open("notes.txt", "w") as f:
    f.write("learning Python is fun!")

with open("notes.txt", "r") as f:
    print(f.read())

with open("tasks.txt", "a") as f:
    f.write("Task Completed!\n")

#problem

import os
import shutil


if not os.path.exists("my_folder"):
    os.mkdir("my_folder")


shutil.copy("notes.txt", "my_folder/notes_copy.txt")


if os.path.exists("tasks.txt"):
    shutil.move("tasks.txt", "my_folder/tasks.txt")


if os.path.exists("my_folder/notes_copy.txt"):
    os.remove("my_folder/notes_copy.txt")


#problem

import sys

def search_word(word, string):
    return string.count(word)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python file.py <filename> <word>")
        sys.exit(1)

    filename = sys.argv[1]
    word = sys.argv[2]

    with open(filename) as f:
        string = f.read()

    n = search_word(word, string)
    print(f"There are {n} occurrences of '{word}' in the file {filename}")
