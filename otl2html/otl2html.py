#!/usr/bin/python
# otl2html.py
# convert a tab-formatted outline from VIM to HTML
#
# Copyright 2001 Cowboyz.com, Inc. All rights reserved
#
# ALPHA VERSION!!!
# $Revision: 1.11 $
# $Date: 2002/01/24 01:09:28 $
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
#	HTML H1 through H9 tags.  Alphabetic, numeric and bullet formats
#	are also supported.
#


###########################################################################
# include whatever mdules we need

import sys
from string import *
from time import *

###########################################################################
# global variables

formatMode = "simple"
level = 0
slides = 0
hideComments = 0
inputFile = ""
outline = []
flatoutline = []

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
   print "otl2html.py [-v]"
   print "    -t     Specify the format type"
   print "    Types: simple - uses HTML tags <H1> through <H9>"
   print "           bullets - uses HTML tags <UL> and <LI>"
   print "           numeric - uses HTML tags <OL> and <LI> for 1.1.1"
   print "           roman - uses HTML tags <OL> and <LI> for I.I.I"
   print "           alpha - uses HTML tags <OL> and <LI> for A.A.A"
   print "    -s     Slide show output for use with HtmlSlides"
   print "    -c     Hide comments (line with [ as the first"
   print "           non-whitespace character. Ending with ] is"
   print "           optional."
   print "    -v     Print version (RCS) information"
   print "output is on STDOUT"
   print

# version
# print the RCS version information
# input: none
# output: RSC version information is printed on the console
 
def showVersion():
   print
   print "RCS"
   print " $Revision: 1.11 $"
   print " $Date: 2002/01/24 01:09:28 $"
   print " $Author: noel $"
   print " $Source: /home/noel/active/projects/NoelOTL/RCS/otl2html.py,v $"
   print

# getArgs
# Check for input arguments and set the necessary switches
# input: none
# output: possible console output for help, switch variables may be set

def getArgs():
  global inputfile, debug, formatMode, slides, hideComments
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
        elif (sys.argv[i] == "-c"):		# test for the comments flag
	  hideComments = 1			# set the comments flag
        elif (sys.argv[i] == "-t"):		# test for the type flag
	  formatMode = sys.argv[i+1]		# get the type
	  i = i + 1				# increment the pointer
        elif (sys.argv[i] == "--help"):
	  showUsage()
	  sys.exit()
        elif (sys.argv[i] == "-h"):
	  showUsage()
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
  return(n+1)					# return the count + 1 (for level)

# getLineTextLevel
# get the level of the current line (count the number of tabs)
# input: linein - a single line that may or may not have tabs at the beginning
# output: returns a number 1 is the lowest

def getLineTextLevel(linein):
  strstart = lstrip(linein)			# find the start of text in line
  x = find(linein,strstart)			# find the text index in the line
  n = count(linein,"\t",0,x)			# count the tabs
  n = n + count(linein," ",0,x)			# count the spaces
  return(n+1)					# return the count + 1 (for level)
    
# processLine
# process a single line
# input: linein - a single line that may or may not have tabs at the beginning
#        format - a string indicating the mode to use for formatting
#        level - an integer between 1 and 9 that show the current level
# 	          (not to be confused with the level of the current line)
# output: through standard out

def processLine(linein):
  global level, formatMode, slides, hideComments
  lineLevel = getLineLevel(linein)
  if ((hideComments == 0) or (lineLevel != (find(linein,"[")+1))):
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
        print
      if (lstrip(rstrip(linein)) == "----------------------------------------"):
        print "<br><br><hr><br>"
      else:
        if (slides == 0):
          if (lineLevel == find(linein," ") +1 ):
  	    print "<p>" + lstrip(linein) + "</p>"
  	  else:
            print "<LI>" + lstrip(linein)
        else:
          if (lineLevel == 1):
            if (linein[0] == " "):
              print "<p>" + lstrip(linein) + "</p>"
            else:
              print "<address>"
	      print lstrip(linein)
	      print "</address>\n"
          else:
            if (lineLevel == find(linein," ") +1):
              print "<p>" + lstrip(linein) + "</p>"
            else:
              print "<LI>" + lstrip(linein)
      
# flatten
# Flatten a subsection of an outline.  The index passed is the outline section
# title.  All sublevels that are only one level deeper are indcluded in the current
# subsection.  Then there is a recursion for those items listed in the subsection.
# Exits when the next line to be processed is of the same or lower outline level.
#  (lower means shallower)
# input: idx - the index into the outline.  The indexed line is the title.
# output: adds reformatted lines to flatoutline[]

def flatten(idx):
  if (outline[idx] == ""):
    return
  if (len(outline) <= idx):
    return
  titleline = outline[idx]
  titlelevel = getLineLevel(titleline)
  if (getLineLevel(outline[idx+1]) > titlelevel):
    if (titleline[titlelevel-1] != " "):
      flatoutline.append(lstrip(titleline))
    exitflag = 0
    while (exitflag == 0):
      if (idx < len(outline)-1):
        idx = idx + 1
        currlevel = getLineLevel(outline[idx])
        if (currlevel == titlelevel + 1):
          if (currlevel == find(outline[idx]," ") +1):
            flatoutline.append("\t " + lstrip(outline[idx]))
          else:
            flatoutline.append("\t" + lstrip(outline[idx]))
        elif (currlevel <= titlelevel):
          exitflag = 1
      else:
        exitflag = 1
  level =  titlelevel
  return

def printHeader(linein):
  print "<HTML><TITLE>" + linein + "</TITLE>"
  print"<!--  $Revsion:$ -->"
  print"<!--  $Date: 2002/01/24 01:09:28 $ -->"
  print"<!--  $Author: noel $ -->"

def printStyle(linein):
  print "<BODY>"
  print "<DIV NAME=\"DocTitle\">"
  print "<H1>" + lstrip(linein) +"</H1>"
  print "</DIV>"
  print "<DIV NAME=\"Main\">"

def printFooter():
  global slides
  print "</DIV>"
  if (slides == 0):
	  print "<br><br><br><font size=1>Copyright (C) 2002 Cowboyz.com, Inc. "
	  print "All Rights Reserved</font><br>"
	  print inputfile + "&nbsp&nbsp " + strftime("%Y/%m/%d %H:%M",localtime(time()))
  print "</BODY></HTML>"

def main():
  getArgs()
  flatouline = []
  file = open(inputfile,"r")
  if (slides == 0):
    firstLine = lstrip(rstrip(file.readline()))
    printHeader(firstLine)
    printStyle(firstLine)
    linein = lstrip(rstrip(file.readline()))
    while linein != "":
      processLine(linein)
      linein = file.readline()
  else:
    linein = lstrip(rstrip(file.readline()))
    outline.append(linein)
    linein = lstrip(rstrip(file.readline()))
    while linein != "":
      outline.append("\t" + linein)
      linein = rstrip(file.readline())
    for i in range (0,len(outline)-1):
      flatten(i)
    printHeader(flatoutline[0])
    printStyle(flatoutline[0])
    for i in range (0,len(flatoutline)):
      processLine(flatoutline[i])
    
  printFooter()
  file.close()

main()
    
