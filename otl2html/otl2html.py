#!/usr/bin/python
# otl2html.py
# convert a tab-formatted outline from VIM to HTML
#
# Copyright 2001 Cowboyz.com, Inc. All rights reserved
#
# ALPHA VERSION!!!
# $Revision: 1.6 $
# $Date: 2001/10/09 22:22:39 $
# $Author: noel $
# $Source: /home/noel/active/projects/NoelOTL/RCS/otl2html.py,v $
# $Locker: noel $

###########################################################################
# Basic function
#
#	This program accepts text outline files and converts them
#	to HTML.  The outline levels are indicated by tabs. A line with no
#	tabs is assumed to be part of the highest outline level.
#
#	10 outline levels are supported.  These loosely correspond to the
#	HTML H1 through H9 tags.
#


###########################################################################
# include whatever mdules we need

import sys
from string import *

###########################################################################
# global variables

formatMode = "simple"
level = 0
slides = 0
inputFile = ""
outline = []

###########################################################################
# function definitions

# usage
# print the simplest form of help
# input: none
# output: simple command usage is printed on the console
 
def showUsage():
   print
   print "Usage:"
   print "otl2html.py inputfile"
   print "otl2html.py [-t type] [-s] inputfile"
   print "    -t     Specify the format type"
   print "    Types: simple - uses HTML tags <H1> through <H9>"
   print "           bullets - uses HTML tags <UL> and <LI>"
   print "           numeric - uses HTML tags <OL> and <LI> for 1.1.1"
   print "           roman - uses HTML tags <OL> and <LI> for I.I.I"
   print "           alpha - uses HTML tags <OL> and <LI> for A.A.A"
   print "    -s     Slide show output for use with htmlslides"
   print "output is on STDOUT"
   print

# getArgs
# Check for input arguments and set the necessary switches
# input: none
# output: possible console output for help, switch variables may be set

def getArgs():
  global inputfile, debug, formatMode, slides
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
        elif (sys.argv[i] == "-s"):		# test for the slides flag
	  slides = 1				# set the slides flag
        elif (sys.argv[i] == "-t"):		# test for the type flag
	  formatMode = sys.argv[i+1]		# get the type
	  i = i + 1				# increment the pointer
        elif (sys.argv[i] == "--help"):
	  showUsage()
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
  return(n+1)					# return the count + 1 (for level)
    
# processLine
# process a single line
# input: linein - a single line that may or may not have tabs at the beginning
#        format - a string indicating the mode to use for formatting
#        level - an integer between 1 and 9 that show the current level
# 	          (not to be confused with the level of the current line)
# output: through standard out

def processLine(linein):
  global level, formatMode, slides
  lineLevel = getLineLevel(linein)
  if (formatMode == "simple"):
    print "<H" + str(lineLevel) + ">" + lstrip(linein) + "</H" + str(lineLevel) + ">"
  else:
    if (lineLevel > level):
      while (lineLevel > level):
	if (formatMode == "bullets"):
	  print "<UL>"
	elif (formatMode == "roman"):
	  print "<OL type=\"I\">"
	elif (formatMode == "numeric"):
	  print "<OL type=\"1\">"
	elif (formatMode == "alpha"):
	  print "<OL type=\"A\">"
	else:
	  sys.exit("Error! Unknown formatMode type")
	level = level + 1
    elif (lineLevel < level):
      while (lineLevel < level):
	if (formatMode == "bullets"):
	  print "</UL>"
	else:
	  print "</OL>"
	level = level - 1
    else:
      print "\n"
    if (rstrip(linein) == "----------------------------------------"):
      print "<br><hr><br>"
    else:
      if (slides == 0):
        print "<LI>" + lstrip(linein)
      else:
        if (lineLevel == 1):
          print "<address>\n" + lstrip(linein) + "</address>"
        else:
          print "<LI>" + lstrip(linein)
      
def printHeader(linein):
  print "<HTML><TITLE>" + linein + "</TITLE>"
  print"<!--  $Revsion:$ -->"
  print"<!--  $Date: 2001/10/09 22:22:39 $ -->"
  print"<!--  $Author: noel $ -->"

def printStyle(linein):
  print "<BODY>"
  #print "<DIV NAME=\"DocTitle\" ALIGN=CENTER>"
  print "<DIV NAME=\"DocTitle\">"
  print "<H1>" + lstrip(linein) +"</H1>"
  print "</DIV>"
  print "<DIV NAME=\"Main\">"


def printFooter():
  print "</DIV></BODY></HTML>"

def main():
  getArgs()
  file = open(inputfile,"r")
  firstLine = lstrip(file.readline())
  printHeader(firstLine)
  printStyle(firstLine)
  linein = lstrip(file.readline())
  while linein != "":
    processLine(linein)
    linein = file.readline()
  printFooter()
  file.close()

main()
    
