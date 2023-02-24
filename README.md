# CS50P Final Project

This was my final project for Harvards course "CS50P - Introduction to Programming with Python".  
The course teached the basic principles of the Python programming language, together with unit testing, typing and best practices.  
The following project was written by me alone and shall showcase that I learned the skills just mentioned. 

## Project Description:

My final project for this course was named **LEAST USED**. This program takes the path of a root directory and recursively searches for the files the user is using the least.  
The usage is determined by the *access time* of the file with the "File least used" beeing the file that has not been accessed for the longest time.  
Apart from the root directory to search in, the file type is specifiable. Furthermore, files older than a specified time of days can be displayed. Again, showing files which have not been accessed for longer than the specified time of days.  
__LEAST USED__ mainly depends on the __os__ module but also uses functionality from the __argparse__, __datetime__, __sys__ and __re__ modules.  
See also `project.py --help`.

## Usage:

The program is run from the terminal using `python project.py`. The `-p` or `--path` flag is required and specifies the root directory to recursively search in.  
Optional flags are `-t` or `--type`, `-nt` or `--nottype` and `-ot` or `--olderthen`. For more on that read the Details.

__Example__: `python project.py -p c:/Users/You/my_folder -t .txt -ot 30`

> __NOTE:__ If running the script with a path containing spaces, surround the path with double quotes.

## Details

### `project.py`

The file `project.py` contains the main functionality of the project. 
Besides the main function, 5 more functions have been implemented:

#### `parse_arguments`

Contains the command-line functionality. Here, flags, descriptions and a `--help` command are implemented using the __argparse__ module.  

#### `get_files`

Searches the specified directory (__default:__ users home directory) *recursively* and returns the full path of all files as a list.

#### filter_files_include

Is executed when the `-t` or `--type` flag is set. Filters all files for the specified file extension (case insensitive).

#### filter_files_exclude

Is executed when the `-nt` or `--nottype` flag is set. Filters all files, excluding the specified file extension (case insesitive)

#### get_oldest_file

Returns the full filepath of the file which has not been accessed for the longest time.

#### get_olderthen_files

Is executed when the `-ot` or `--olderthen` flag is set. Returns the full filepath of the files which have not been accessed for the number of days specified.

### test_project.py
Contains the unit test for project.py using the __pytest__ module. Tested are the functions `get_files`, `filter_files_include` and `filter_files_exclude`.

### Design choices:

Theoretically, the program could be sped up if the sorted files list from `get_oldest_file` is passed down to the `get_olderthen_files` function. This way, `get_olderthen_files` could break after reaching the first value with an *accesstime* younger then the specified `older_then`, therefore limiting the amount of iterations. However, due to better readability and function testing the current structure was kept. Due to the same reasons `filter_files_include` and `filter_files_exclude` were implemented as seperate functions, rather than implementing them directly into `get_files`.
