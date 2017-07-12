# Password Strength Calculator

This script evaluate password with some criterions such as:
* use of both upper-case and lower-case letters; 
* inclusion numerical digits;
* inclusion of special characters;
* password length;
* unique letters quantity;
* duplicates;
* and words from password blacklist as option. 

# Quickstart

You will need python 3.5 interpreter. Then you can launch 
script in terminal or import functions in your code. 

launch on Linux, Python 3.5:

```#!bash

$ python3 password_strength.py [<path to blacklist file for check>]

#input output example
Input your password: dbfblllfv;4
Password rating - 6
1 - very weak; 10 - cool

Input your password: Password 
Password rating - 1
1 - very weak; 10 - cool
```

Example of blacklist file, use simple text file, one word in one line:
```
123456
admin
password
test
123
123456789
12345678
```
 
Example of using functions in code:

```
import password_strength

rating = get_password_strength(password)

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
