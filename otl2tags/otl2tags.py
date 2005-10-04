#!/usr/bin/python
# otl2tags.py
# Convert an OTL file to any tags-based file using config user-
# definable configuration files. HTML, OPML, XML, LATEX and
# many, many others should be easily supportables.
#
# Copyright (c) 2005 Noel Henson All rights reserved
#
# ALPHA VERSION!!!
# $Revision: 1.2 $
# $Date: 2005/09/25 14:24:28 $
# $Author: noel $
# $Source: /home/noel/active/otl2table/RCS/otl2table.py,v $
# $Locker:  $

###########################################################################
# Basic function
#
#	This program accepts text outline files in Vim Outliners .otl format
#	and converts them to a tags-based equivalent

###########################################################################
# Change Log
#
#	$Log:$

###########################################################################
# include whatever mdules we need

import sys
from string import *
from ConfigParser import *
from re import *

###########################################################################
# global v

level = 0
inputFile = ""
lines = []
config = ConfigParser()
debug = 0
v = {}				# outline variables
linePtr = 0

###########################################################################
# function definitions

# usage
# print the simplest form of help
# input: none
# output: simple command usage is printed on the console
 
def showUsage():
	 print
	 print "Usage:"
	 print "otl2table.py [options] inputfile"
	 print "Options"
	 print "    -c             config-file"
	 print "    -d             debug"
	 print "    --help         show help"
	 print "    -v              Print version (RCS) information."
	 print "output filenames are based on the input file name and the config file"
	 print

# version
# print the RCS version information
# input: none
# output: RSC version information is printed on the console
 
def showVersion():
	 print
	 print "RCS"
	 print " $Revision: 1.2 $"
	 print " $Date: 2005/09/25 14:24:28 $"
	 print " $Author: noel $"
	 print " $Source: /home/noel/active/otl2table/RCS/otl2table.py,v $"
	 print

# getArgs
# Check for input arguments and set the necessary switches
# input: none
# output: possible console output for help, switch variables may be set

def getArgs():
	global inputfile, debug, noTrailing, formatMode, config
	if (len(sys.argv) == 1): 
	  showUsage()
	  sys.exit()()
	else:
	  for i in range(len(sys.argv)):
	    if (i != 0):
	      if (sys.argv[i] == "-c"):	                	# test for the type flag
	         config.read(sys.argv[i+1])      		# read the config
	         i = i + 1			        	# increment the pointer
	      elif (sys.argv[i] == "-d"):
	         debug = 1
	      elif (sys.argv[i] == "-?"):			# test for help flag
	         showUsage()					# show the help
	         sys.exit()					# exit
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
	      else: 					       # get the input file name
	        inputfile = sys.argv[i]

# printConfig
# Debugging routine to print the parsed configuration file
# input: none
# output: configuration data printed to console

def printConfig():
  global config
  print"Config ---------------------------------------------"
  list = config.sections()
  for i in range(len(list)):
	  print
	  print list[i]
	  for x in config.options(list[i]):
	    if (x !="name") and (x !="__name__"):
	      print x,":", config.get(list[i],x)
  print 

# readFile
# read the selected file into lines[]
# input: filename to be loaded
# output: a loaded-up lines[]

def readFile(inputfile):
	global lines
	file = open(inputfile,"r")
	linein = file.readline()
	while linein != "":
	  lines.append(linein)
	  linein = file.readline()
	return
	file.close

# initVariables
# initialize the document v
# input: global dictionary 'v'
# output: global dictionary 'v'

def initVariables():
	global v
	v["%l"] = "0"	# outline level (depth)
	v["%%"] = ""	# object text
	v["%t"] = ""	# document title (the first line)

# getLevel
# get the level of the line specified by linenum
# input: linenum - the number of the line to test
# output: returns the level number, 1 is the lowest

def indentLevel(linenum):
	global lines
	line = lines[linenum]
	strstart = line.lstrip()		# find the start of text in line
	x = find(line,strstart)			# find the text index in the line
	n = count(line,"\t",0,x)			# count the tabs
	n = n + count(line," ",0,x)			# count the spaces
	return(n+1)					# return the count + 1 (for level)

# getLineType
# return the type of the line specified by linenum
# input: linenum - the number of the line to test
# output: returns text, usertext, table, preftext, etc.

def getLineType(linenum):
	global lines
	line = lines[linenum].lstrip()
	if (line[0] == ':'): return 'text'
	elif (line[0] == ';'): return 'preftext'
	elif (line[0] == '>'): return 'usertext'
	elif (line[0:4] == '<cmd'): return 'command'
	elif (line[0] == '<'): return 'userpreftext'
	elif (line[0] == '|'): return 'table'
	elif (line[0] == ''): return 'blank'
	else: return 'heading'

# getHeadingType
# return the heading type of the line specified by linenum
# input: linenum - the number of the line to test
# output: returns bulletedlist, numberedlist, etc.

def getHeadingType(linenum):
	global lines
	line = lines[linenum].lstrip()
	if (line[0] == '-'): return 'bulletedlist'
	elif (line[0] == '+'): return 'numberedlist'
	else: return 'normal'

# getTableType
# return the table type of the line specified by linenum
# input: linenum - the number of the line to test
# output: returns table, tableheader

def getTableType(linenum):
	global lines
	line = lines[linenum].lstrip()
	if (line[0:2] == '||'): return 'tableheader'
	else: return 'tablerow'

# prevHeading
# return the line number of the previous heading
# input: linenum - the number of the line to test
# output: number of previous heading

def prevHeading(linenum):
	global lines
	for i in range(linenum-1,0,-1):
		if (getLineType(i) == 'heading'): return i
	return 0

# nextHeading
# return the line number of the next heading
# input: linenum - the number of the line to test
# output: number of next heading

def nextHeading(linenum):
	global lines
	for i in range(linenum+1,len(lines)):
		if (getLineType(i) == 'heading'): return i
	return 0

# isParent
# determine if the line is a parent
# input: linenum - the number of the line to test
# output: returns 1 if a parent, 0 if not

def isParent(linenum):
	global lines
	if (linenum < len(lines) - 1):
		next = nextHeading(linenum)
		if (indentLevel(linenum) < indentLevel(next)): return 1
		else: return 0
	else: return 0


# isFirstChild
# determine if the line is the first child of a parent
# input: linenum - the number of the line to test
# output: returns 1 if the first child, 0 if not

def isFirstChild(linenum):
	global lines
	if (linenum < len(lines)):
		prev = prevHeading(linenum)
		if (indentLevel(linenum) > indentLevel(prev)): return 1
		else: return 0
	else: return 0

# isLastChild
# determine if the line is the last child of a parent
# input: linenum - the number of the line to test
# output: returns 1 if the last child, 0 if not

def isLastChild(linenum):
	if (linenum < len(lines)):
		next = nextHeading(linenum)
		if (indentLevel(linenum) > indentLevel(next)): return 1
		else: return 0
	else: return 0

# isFirstTableLine
# determine if the line is the first line of a table
# input: linenum - the number of the line to test
# output: returns 1 if the first table line, 0 if not

def isFirstTableLine(linenum):
	global lines
	if (linenum < len(lines)):
		if getLineType(linenum-1) == 'table': return 1
		else: return 0
	else: return 0

# isLastTableLine
# determine if the line is the last line of a table
# input: linenum - the number of the line to test
# output: returns 1 if the last table line, 0 if not

def isLastTableLine(linenum):
	if (linenum < len(lines)):
		if getLineType(linenum+1) != 'table': return 1
		else: return 0
	else: return 0

# isFirstTextLine
# determine if the line is the first line of a text
# input: linenum - the number of the line to test
# output: returns 1 if the first text line, 0 if not

def isFirstTextLine(linenum):
	global lines
	if (linenum < len(lines)):
		if getLineType(linenum-1) == 'text': return 1
		else: return 0
	else: return 0

# isLastTextLine
# determine if the line is the last line of a text
# input: linenum - the number of the line to test
# output: returns 1 if the last text line, 0 if not

def isLastTextLine(linenum):
	if (linenum < len(lines)):
		if getLineType(linenum+1) != 'text': return 1
		else: return 0
	else: return 0

# isFirstPrefTextLine
# determine if the line is the first line of a preftext
# input: linenum - the number of the line to test
# output: returns 1 if the first preftext line, 0 if not

def isFirstPrefTextLine(linenum):
	global lines
	if (linenum < len(lines)):
		if getLineType(linenum-1) == 'preftext': return 1
		else: return 0
	else: return 0

# isLastPreftextLine
# determine if the line is the last line of a preftext
# input: linenum - the number of the line to test
# output: returns 1 if the last preftext line, 0 if not

def isLastPrefTextLine(linenum):
	if (linenum < len(lines)):
		if getLineType(linenum+1) != 'preftext': return 1
		else: return 0
	else: return 0

# isFirstUsertextLine
# determine if the line is the first line of a preftext
# input: linenum - the number of the line to test
# output: returns 1 if the first preftext line, 0 if not

def isFirstUserpreftextLine(linenum):
	global lines
	if (linenum < len(lines)):
		if getLineType(linenum-1) == 'userpreftext': return 1
		else: return 0
	else: return 0

# isLastUsertextLine
# determine if the line is the last line of a preftext
# input: linenum - the number of the line to test
# output: returns 1 if the last preftext line, 0 if not

def isLastUserPreftextLine(linenum):
	if (linenum < len(lines)):
		if getLineType(linenum+1) != 'userpreftext': return 1
		else: return 0
	else: return 0

# subVars
# substitute variables in output expressions
# input: section - section from config
# input: type - object type (to look up in config)
# input:  - substitution item (by name) from config array
# output: string - the substitution expression with variables inserted

def subVars(section,type):
	global config, v

	varlist = v.keys()
	pattern = config.get(section,type)

	for var in varlist:
		x = ""
		x = var
		y = ""
		y = v.get(var)
		pattern = sub(x,y,pattern)
#		pattern = sub(varlist[i],v[varlist[i]],pattern)
#		print pattern
	return pattern

###########################################################################
# Main Program Loop

def main():
	global inputfile, lines, debug, v, linePtr
	getArgs()
	if (debug !=0): printConfig()
	initVariables()
	readFile(inputfile)
	v["%t"] = lines[0]

	for i in range(1,len(lines)):
		print lines[i],

		v["%l"] = str(i)
		v["%%"] = lstrip(rstrip(lines[i]))
		print subVars("Headings","heading")

		print getLineType(i),
		if (getLineType(i) == 'heading'):
			print getHeadingType(i),
		if (getLineType(i) == 'table'):
			print getTableType(i),
		if (isFirstChild(i)): print "first_child",
		if (isLastChild(i)): print "last_child",
		if (isParent(i)): print "Parent",
		print

main()
