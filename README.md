 ![Image of holb](https://camo.githubusercontent.com/8d76bb2b9f2eeeb22ba9236805e758b58eb7fdc4/68747470733a2f2f696d6775722e636f6d2f4f696c457358562e706e67)

---
# HBnB the Console!

## AirBnB clone, first part, the console

---

Description

>We will create a storage system, creating objects through execution and saving them to a Js. We will manipulate two types of storage, file and DataBase, for this projecy we will focus on file.
---
### Program download
>To download this program, you must go to this github repo and download it:

    https://github.com/julianramirezch/AirBnB_clone/blob/master/README.md

>Once in your local repo, you can run it from the folder using the following command:

    ./console.py

### Execution:
>There are two modes
    
    Interactive mode:
>$ ./console.py

    $  (hbnb) [write here your commands]

>Non-interactive mode

    $ echo "[put_commands and_arguments]" | ./console.py

### Commands

    • help
    • EOF
    • quit
    • create
    • show
    • destroy
    • all
    • update
    • count
### Examples
    1. help
    • non interactive

$ echo "help" | ./console.py

    $ (hbnb) 
    Documented commands (type help <topic>):
    ========================================
    EOF  all  count  create  destroy  help  quit  show  update

    (hbnb)


    • interactive mode

>$ ./console.py

     (hbnb) help

>(hbnb)
>Documented commands (type help <topic>):
>========================================
>EOF  all  count  create  destroy  help  quit  show  update
>(hbnb)

    (hbnb) quit

$
### Some error output

>$ ./console.py

    (hbnb) all MyModel
    ** class doesn't exist **
    (hbnb) show BaseModel
    ** instance id missing **
    (hbnb) show BaseModel Holberton
    ** no instance found **

### Project files

|:- File      -:|:- Description -: |
|:------------ | ----------: |
| AUTHORS     | File names and email of project’s owners|
Readme.md |Description and examples of project|
|console.py | command interpreter file 
|| Class HBNBcommand - console and commands |
| _free_data.c  |Frees data allocated |
|| _free - frees all data|
|| free_env - frees enviroment variable |
|| free_args - Frees double pointer |
|| free_all - calls all free functions |
|| free_array - frees arrays |
| _getenv.c | functions that get enviroment and handle it |
| | _getenv |
|| free_PATH - frees PATH variable |
|| _myenv2 | prints env variable |
| _launch.c | executes command line |
| builtins.c | contains builtin functions |
|| _cd |
|| _help |
|| printwd |
|| myexit |
| exec_path.c | contains function that reads and executes path|
| get_help.c | aux functions for help builtin|
|| get_help |
|| more_help |
| handle_input.c | functions that read and parse the command line|
|init_data.c | data initialization at start of program |
| loop_prompt.c | displays prompt |
| main.c | main function that calls all other functions |
| shell.h | header |





   
    How to create a Python package
    How to create a command interpreter in Python using the cmd module
    What is Unit testing and how to implement it in a large project
    How to serialize and deserialize a Class
    How to write and read a JSON file
    How to manage datetime
    What is an UUID
    What is *args and how to use it
    What is **kwargs and how to use it
    How to handle named arguments in a function


### Tasks:

| Name | Description                    |
| ------------- | ------------------------------ |
| `__init__.py`      |  With this file, the folder will become a Python module   |
| `models/base.py`      |    Class Base |
| `models/rectangle.py`   | Class Rectangle   |
| `models/square.py`      | Class Square|
| `tests/test_models/test_base.py`      | Test Class Base |
| `tests/test_models/test_rectangle.py`      |  Test Class Rectangle   |
| `tests/test_models/test_square.py`      |  Test Class Square   |

## Author: 
### Julian Ramirez <julianramirezch1@gmail.com>
### Santiago Mendieta <santmendieta@icloud.com>
----
[![Twitter Follow](https://img.shields.io/twitter/follow/JulianR_30.svg?style=social&label=Follow)](https://twitter.com/JulianR_30)

2020
