#!/usr/bin/python
# otlslit.py
# split an outline into several files.
#
# Copyright 2005 Noel Henson All rights reserved
#
# $Revision: 1.43 $
# $Date: 2005/06/07 13:16:40 $
# $Author: noel $
# $Source: /home/noel/active/NoelOTL/RCS/otl2html.py,v $
# $Locker:  $

###########################################################################
# Basic function
#
#	This program accepts text outline files and splits them into
#	several smaller files. The output file names are produced from the
#	heading names of the parents.
#

###########################################################################
# include whatever mdules we need

import sys
from string import *
from re import *

###########################################################################
# global variables

debug = 0
level = 0
inputfile = ""

###########################################################################
# function definitions

# usage
# print the simplest form of help
# input: none
# output: simple command usage is printed on the console
 
def showUsage():
   print
   print "Usage:"
   print "otlsplit.py [options] inputfile > outputfile"
   print "Options"
   print "    -l level        The number of levels to split down to. The default is 1"
   print "    -v              Print version (RCS) information."
   print "    -H              Show the file syntax help."
   print "output is on STDOUT"
   print

# version
# print the RCS version information
# input: none
# output: RSC version information is printed on the console
 
def showVersion():
   print
   print "RCS"
   print " $Revision: 1.43 $"
   print " $Date: 2005/06/07 13:16:40 $"
   print " $Author: noel $"
   print

# getArgs
# Check for input arguments and set the necessary switches
# input: none
# output: possible console output for help, switch variables may be set

def getArgs():
  global debug, level, inputfile
  if (len(sys.argv) == 1): 
    showUsage()
    sys.exit()()
  else:
    for i in range(len(sys.argv)):
      if (i != 0):
        if   (sys.argv[i] == "-d"): debug = 1	# test for debug flag
        elif (sys.argv[i] == "-?"):		# test for help flag
	  showUsage()				# show the help
	  sys.exit()				# exit
        elif (sys.argv[i] == "-l"):		# test for the style sheet flag
	  level = sys.argv[i+1]			# get the style sheet name
	  i = i + 1				# increment the pointer
        elif (sys.argv[i] == "--help"):
	  showUsage()
	  sys.exit()
        elif (sys.argv[i] == "-h"):
	  showUsage()
	  sys.exit()
        elif (sys.argv[i] == "-H"):
	  showSyntax()
	  sys.exit()
        elif (sys.argv[i] == "-v"):
	  showVersion()
	  sys.exit()
	elif (sys.argv[i][0] == "-"):
	  print "Error!  Unknown option.  Aborting"
	  sys.exit()
	else: 					# get the input file name
          inputfile = sys.argv[i]

# getLineLevel
# get the level of the current line (count the number of tabs)
# input: linein - a single line that may or may not have tabs at the beginning
# output: returns a number 1 is the lowest

def getLineLevel(linein):
  strstart = lstrip(linein)			# find the start of text in line
  x = find(linein,strstart)			# find the text index in the line
  n = count(linein,"\t",0,x)			# count the tabs
  return(n)					# return the count + 1 (for level)

# convertSensitiveChars
# get the level of the current line (count the number of tabs)
# input: line - a single line that may or may not have tabs at the beginning
# output: returns a string

def convertSensitiveChars(line):
  line = lstrip(rstrip(line))
  line = sub('\W','_',line)
  return(line)					# return the count + 1 (for level)

# makeFileName
# make a file name from the string array provided
# input: line - a single line that may or may not have tabs at the beginning
# output: returns a string

def makeFileName(nameParts):

  global debug, level

  filename = ""
  for i in range(level):
	  filename = filename + lstrip(rstrip(nameParts[i]))
  return(filename)				# return the count + 1 (for level)

# processFile
# split an outline file
# input: file - the filehandle of the file we are splitting
# output: output files

def processFile(file)

  global debug, level

  nameparts = []
  outOpen = 0

  line = file.readline()			# read the outline title
  						# and discard it
  line = file.readline()			# read the first parent heading
  while (line !=""):
	  linelevel = getLineLevel(line)
	  if (linelevel < level):
		if outOpen == 1: 
			ofile.close()
			outOpen = 0
	  	nameparts[linelevel] = convertSensitiveChars(line)
	  else:
		  if outOpen == 0: 
			  ofile = open(makeFileName(nameParts),"w")
			  outOpen = 1
		  ofile.write(line[level:])
	  line = file.readline()
	
# main
# split an outline
# input: args and input file
# output: output files

def main():
  global inputfile, debug
  getArgs()
  file = open(inputfile,"r")
  processFile(file)  
  file.close()

main()
    
