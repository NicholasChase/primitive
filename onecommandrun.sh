#!/bin/sh
#This program is designed to run primitive in one command when user wants to 
#run basic primitive
#must have go installed for this to work
go get -u github.com/fogleman/primitive
primitive -i input.png -o output.png -n 100
