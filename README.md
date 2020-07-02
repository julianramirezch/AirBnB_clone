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

    https://github.com/matcls/simple_shell

>Once in your local repo, you can complile it with the following command:

    gcc -Wall -Werror -Wextra -pedantic *.c

### Execution:
>There are two modes
    
    Interactive mode:
>$ ./a.out

    $ [write here your commands]

>Non-interactive mode

    $ echo "[put_commands and_arguments]" | ./a.out

### Built-ins

    • env
    • exit
    • help
    • pwd
### Examples
    1. Absolute path commands
    • non interactive

$ echo "/bin/pwd" | ./a.out

    $ /home/simple_shell

    • interactive mode

>$ ./a.out

    ./$ /bin/ls

>simple_shell.c

./$ exit

$

    2. short command
    • non interactive

$ echo "pwd" | ./a.out

>$ /home/simple_shell

    • interactive mode

>$ ./a.out

    ./$ echo welcome to shell

>welcome to shell

    ./$ exit

>$

    3. built-ins
    • non interactive

$ echo "pwd" | ./a.out

    $ echo "pwd" | ./a.out

    • interactive mode

>$ ./a.out

    ./$ cd
>$ pwd

    /home

### Some error output

>$ ./a.out

    ./$ cd..

>command not found: cd..

    $ ..

>$  ..: Permission denied

    2

---
### Project files

|:- File      -:|:- Description -: |
|:------------ | ----------: |
| AUTHORS     | File names and email of project’s owners|
Readme.md |Description and examples of project|
|_dupenv.c | Enviroment variable duplicate 
|| _dupenv - duplicates enviroment variables |
|_execute.c | Finds and executes commands |
| | find_command – finds function from command line |
|| _executes: sorts if builtin or PATH |
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







### Manual page

You can find all the information on our man page

    $ ./man_1_simple



>Flow chart an be found at this address:

>>https://app.diagrams.net/#G1LC_F4Ss5qHXNA5NKIuUAo5PHcCVRhmeV



   
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
