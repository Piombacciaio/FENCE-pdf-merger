# Fence pdf merger

Since the program in use to manage fencing competitions can not export a single pdf for each category of athletes this makes uploading results quite tedious and this script solves the problem.

This prelude just to say that this is a basic pdf merger that collects all the pdfs that match a certain naming from a folder and merge them into a single file with the same name as the directory,
then moves the original folder to a "completed" folder to store the partial files and the output to a selected folder

## Requirements

- [Python 3.x](https://www.python.org/downloads/)
- pip requirements (`pip install -U -r requirements.txt`)
