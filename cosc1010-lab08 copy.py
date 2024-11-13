# Ryan Dennis
# UWYO COSC 1010
# Submission Date 11/12/2024
# Homework 4 
# Lab Section: 14
# Sources, people worked with, help given to: w3schools.com, Geeks for Geeks, Stack Overflow
# your
# comments
# here

from pathlib import Path
path = Path('prompt.txt')
contents = path.read_text()
lines = contents.splitlines()
art = open("art","a")
for line in lines:
    prompt = line.split("\t")
    to_write = " "
    for item in prompt:
        if "w" in item:
            w_numbers = item.split(":")
            space_numbers = int(w_numbers[1])
            whitespace = " " * space_numbers
            to_write += whitespace
        elif "*" in item:
            dot_numbers = item.split(":")
            total_dots = int(dot_numbers[1])
            dot = "*" * total_dots
            to_write += dot
    art.write(to_write + "\n")
