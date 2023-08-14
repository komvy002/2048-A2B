# INFS2048 SP1 2023 Source Code Instructions

This directory contains the provided source code for Assignment 2.

## Code
File word\_statistics\_app.py is the main entry point for this application. 
The provided code handles all the command line interaction for this application. 
You will, of course, need to extend its main() function to implement the system.

## Example
There are example input and output files to illustrate the computation the program will need to accomplish.
The contents of out.txt and out.csv shows the expected output of the program when invoked as follows:

    $ python word_statistics_app.py --number=5 --output=out.txt --output=out.csv in1.txt in2.txt


## Prerequisites
This code requires Python >=3.10 and the _click_ package  (which handles the command line interaction).
Please follow your Python environment's guidelines for installing this package.

Common ways to install this package are via pip or conda:

    $ pip install -r requirements.txt

    $ conda install --file requirements.txt


