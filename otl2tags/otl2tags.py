#!/usr/bin/python
# otl2tags.py
# Convert an OTL file to any tags-based file using config user-
# definable configuration files. HTML, OPML, XML, LATEX and
# many, many others should be easily supportables.
#
# Copyright (c) 2005 Noel Henson All rights reserved
#
# ALPHA VERSION!!!
# $Revision: 1.3 $
# $Date: 2005/10/18 16:01:15 $
# $Author: noel $
# $Source: /home/noel/active/otl2tags/RCS/otl2tags.py,v $
# $Locker:  $

###########################################################################
# Basic function
#
#	This program accepts text outline files in Vim Outliners .otl format
#	and converts them to a tags-based equivalent

###########################################################################
# Change Log
#
#	$Log: otl2tags.py,v $
#	Revision 1.3  2005/10/18 16:01:15  noel
#	First completely working version.
#
#	Revision 1.2  2005/10/18 10:32:28  noel
#	Works except for leaving levels and some other minutia.
#
#	Revision 1.1  2005/10/04 13:08:21  noel
#	Initial revision
#

###########################################################################
# include whatever mdules we need

import sys
from string import *
from ConfigParser import *
from re import *

###########################################################################
# global variables

level = 0
exitlevel = 0
inputFile = ""
lines = []
parents = []
config = ConfigParser()
debug = 0
linePtr = 0
v = {}				# outline variables
text = ""

###########################################################################
# function definitions

# usage
# print debug statements
# input: string
# output: string printed to standard out

def dprint(*vals):
	global debug
	if debug != 0: print vals

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
	 print " $Revision: 1.3 $"
	 print " $Date: 2005/10/18 16:01:15 $"
	 print " $Author: noel $"
	 print " $Source: /home/noel/active/otl2tags/RCS/otl2tags.py,v $"
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
  print"----------------------------------------------------"
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
	v["%n"] = "0"	# line number
	v["%N"] = "0"	# line number for first line of text block
	v["%p"] = "0"	# parent line number
	v["%l"] = "0"	# outline level (depth)
	v["%%"] = ""	# object text
	v["%t"] = ""	# document title (the first line)

# lfStrip(line)
# strip the trailing lf from the line
# input: line
# output: returns a string with a stripped 'lf'

def lfStrip(line):
	return rstrip(line,'\n')

# colonStrip(line)
# strip a leading ':', if it exists
# input: line
# output: returns a string with a stripped ':'

def colonStrip(line):
	if (line[0] == ":"): return lstrip(line,': ')
        else: return line

# semicolonStrip(line)
# strip a leading ';', if it exists
# input: line
# output: returns a string with a stripped ';'

def semicolonStrip(line):
	if (line[0] == ";"): return lstrip(line,'; ')
        else: return line

# dashStrip(line)
# strip a leading '-', if it exists
# input: line
# output: returns a string with a stripped '-'

def dashStrip(line):
	if (line[0] == "-"): return lstrip(line[1:])
        else: return line

# greaterStrip(line)
# strip a leading '>', if it exists
# input: line
# output: returns a string with a stripped '>'

def greaterStrip(line):
	if (line[0] == ">"): return lstrip(line,'> ')
        else: return line

# lessStrip(line)
# strip a leading '<', if it exists
# input: line
# output: returns a string with a stripped '<'

def lessStrip(line):
	if (line[0] == "<"): return lstrip(line,'< ')
        else: return line

# pipeStrip(line)
# strip a leading '|', if it exists
# input: line
# output: returns a string with a stripped '|'

def pipeStrip(line):
	if (line[0] == "|"): return lstrip('|')
        else: return line

# plusStrip(line)
# strip a leading '+', if it exists
# input: line
# output: returns a string with a stripped '+'

def plusStrip(line):
	if (line[0] == "+"): return lstrip(line[1:])
        else: return line

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
	if (line[0] == '-'): return 'bulleted'
	elif (line[0] == '+'): return 'numbered'
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

# nextHeadingAtLevel
# return the line number of the next heading
# input: linenum - the number of the line to test
# output: number of next heading

def nextHeadingAtLevel(linenum,lvl):
	global lines
	for i in range(linenum+1,len(lines)):
		if (getLineType(i) == 'heading') and (indentLevel(i) <= lvl): return i
	return 0


# isParent
# determine if the line is a parent
# input: linenum - the number of the line to test
# output: returns 1 if a parent, 0 if not

def isParent(linenum):
	global lines
	if (linenum < len(lines) - 1):
		if (indentLevel(linenum) < indentLevel(linenum+1)): return 1
		else: return 0
	else: return 0


# isFirstChild
# determine if the line is the first child of a parent
# input: linenum - the number of the line to test
# output: returns 1 if the first child, 0 if not

def isFirstChild(linenum):
	global lines
	if linenum == 1: return 1
	if (linenum < len(lines)):
		prev = prevHeading(linenum)
		if (indentLevel(linenum) > indentLevel(prev)): return 1
		else: return 0
	else: return 0

# isLastChild
# determine if the line is the last child of a parent
# input: linenum - the number of the line to test
# input: mylevel - the level of heading
# output: returns 1 if the last child, 0 if not

def isLastChild(linenum,mylevel):
	global lines
#	if (linenum < len(lines)):
#		next = nextHeadingAtLevel(linenum,mylevel)
#		dprint("nx:",next,"lpl:",indentLevel(linenum),"nxl:",indentLevel(next))
#		if (mylevel > indentLevel(next)): return 1
#		else: return 0
#	else: return 0
	if linenum == len(lines)-1: return 0
	elif mylevel>=indentLevel(linenum+1): 
		return 1
	else: return 0

# isFirstTableLine
# determine if the line is the first line of a table
# input: linenum - the number of the line to test
# output: returns 1 if the first table line, 0 if not

def isFirstTableLine(linenum):
	global lines
	if (linenum < len(lines)):
		if getLineType(linenum-1) != 'table': return 1
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
		if getLineType(linenum-1) != 'text': return 1
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
		if getLineType(linenum-1) != 'preftext': return 1
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

# isFirstUserPrefTextLine
# determine if the line is the first line of a preftext
# input: linenum - the number of the line to test
# output: returns 1 if the first preftext line, 0 if not

def isFirstUserPrefTextLine(linenum):
	global lines
	if (linenum < len(lines)):
		if getLineType(linenum-1) != 'userpreftext': return 1
		else: return 0
	else: return 0

# isLastUserPreftextLine
# determine if the line is the last line of a preftext
# input: linenum - the number of the line to test
# output: returns 1 if the last preftext line, 0 if not

def isLastUserPrefTextLine(linenum):
	if (linenum < len(lines)):
		if getLineType(linenum+1) != 'userpreftext': return 1
		else: return 0
	else: return 0

# isFirstUserTextLine
# determine if the line is the first line of a preftext
# input: linenum - the number of the line to test
# output: returns 1 if the first preftext line, 0 if not

def isFirstUserTextLine(linenum):
	global lines
	if (linenum < len(lines)):
		if getLineType(linenum-1) != 'usertext': return 1
		else: return 0
	else: return 0

# isLastUsertextLine
# determine if the line is the last line of a preftext
# input: linenum - the number of the line to test
# output: returns 1 if the last preftext line, 0 if not

def isLastUserTextLine(linenum):
	if (linenum < len(lines)):
		if getLineType(linenum+1) != 'usertext': return 1
		else: return 0
	else: return 0

# subVars
# substitute variables in output expressions
# input: section - section from config
# input: type - object type (to look up in config)
# input:  - substitution item (by name) from config array
# output: string - the substitution expression with variables inserted

def subVars(section,type):
	global config, v, linePtr, level, lines, parents

	varlist = v.keys()
	pattern = config.get(section,type)
	v["%n"] = str(linePtr)
	v["%l"] = str(level)
	if len(parents) > 0:
		v["%p"] = str(parents[len(parents)-1])
	# v["%%"] = lstrip(rstrip(lines[linePtr])) - this should be done in handling

	for var in varlist:
		x = ""
		x = var
		y = ""
		y = v.get(var)
		pattern = sub(x,y,pattern)
	return pattern

# handleHeading()
# process a heading object and print a converted version of it
# input: globals
# output: standard out

def handleHeading():

	global linePtr, lines, level, v, exitlevel, parents

	v["%%"] = lstrip(rstrip(lines[linePtr]))
	if getHeadingType(linePtr) == 'normal':
		if isFirstChild(linePtr): 
			level = level + 1
			print subVars("Headings","before-headings")
		print subVars("Headings","heading")
		if isParent(linePtr):
			parents.append(linePtr)
			linePtr = linePtr + 1
			dprint("ho:",linePtr)
			handleObjects()
			dprint("xl:",level)
		dprint("lp:",linePtr,"ml:",level)
		if isLastChild(linePtr,level): 
			print subVars("Headings","after-headings")
			level = level - 1
			exitlevel = 1
			dprint("lc")
			parents.pop()
	elif getHeadingType(linePtr) == 'bulleted':
		v["%%"] = dashStrip(v["%%"])
		if isFirstChild(linePtr): 
			level = level + 1
			print subVars("Headings","before-bulleted-headings")
		print subVars("Headings","bulleted-heading")
		if isParent(linePtr):
			parents.append(linePtr)
			linePtr = linePtr + 1
			handleObjects()
		if isLastChild(linePtr,level): 
			print subVars("Headings","after-bulleted-headings")
			level = level - 1
			exitlevel = 1
			parents.pop()
	elif getHeadingType(linePtr) == 'numbered':
		v["%%"] = plusStrip(v["%%"])
		if isFirstChild(linePtr): 
			level = level + 1
			print subVars("Headings","before-numbered-headings")
		print subVars("Headings","numbered-heading")
		if isParent(linePtr):
			parents.append(linePtr)
			linePtr = linePtr + 1
			handleObjects()
		if isLastChild(linePtr,level): 
			print subVars("Headings","after-numbered-headings")
			level = level - 1
			exitlevel = 1
			parents.pop()
	else: 
		print
		print "Error: unknown heading type"
		sys.exit(1)

# handleText()
# process a block of body text and output a converted version of it
# input: globals
# output: standard out

def handleText():

	global linePtr, lines, level, v, text

	v["%%"] = lfStrip(colonStrip(lstrip(rstrip(lines[linePtr],'\n'))))
	
	if isFirstTextLine(linePtr):
		level = level + 1
		text = subVars("Text","before-text")
		v["%N"] = str(linePtr)
	if lstrip(rstrip(lines[linePtr])) == ":":
		text += subVars("Text","paragraph-sep")
	else:
		text += subVars("Text","text")
	if isLastTextLine(linePtr): 
		text += subVars("Text","after-text")
		print text
		text = ""
		level = level - 1
		exitlevel = 1

# isAlignRight
# return flag
# input: coldata, a string

def isAlignRight(coldata):
  l = len(coldata)
  if (coldata[0:2] == "  ") and (coldata[l-2:l] != "  "): return 1
  else: return 0

# isAlignLeft
# return flag
# input: coldata, a string

def isAlignLeft(coldata):
  l = len(coldata)
  if (coldata[0:2] != "  ") and (coldata[l-2:l] == "  "): return 1
  else: return 0

# isAlignCenter
# return flag
# input: coldata, a string

def isAlignCenter(coldata):
  l = len(coldata)
  if (coldata[0:2] == "  ") and (coldata[l-2:l] == "  "): return 1
  else: return 0

# handleTableColumns
# process a table row's columns and output the converted data
# input: globals
# output: standard out

def handleTableRow():
	
	coldata = lstrip(rstrip(v["%%"]))
	coldata = coldata.split("|")
	print subVars("Tables","before-table-row")
	for i in range(1,len(coldata)):
		v["%%"] = lstrip(rstrip(coldata[i]))
		if isAlignCenter(coldata[i]): print subVars("Tables","table-column-center")
		elif isAlignRight(coldata[i]): print subVars("Tables","table-column-right")
		elif isAlignLeft(coldata[i]): print subVars("Tables","table-column-left")
		else:  print subVars("Tables","table-column")
	print subVars("Tables","after-table-row")

# handleTableHeaderColumns
# process a table row's columns and output the converted data
# input: globals
# output: standard out

def handleTableHeader():
	
	coldata = lstrip(rstrip(v["%%"]))
	coldata = coldata.split("|")
	print subVars("Tables","before-table-header")
	for i in range(2,len(coldata)):
		v["%%"] = lstrip(rstrip(coldata[i]))
		if isAlignCenter(coldata[i]): print subVars("Tables","table-header-column-center")
		elif isAlignRight(coldata[i]): print subVars("Tables","table-header-column-right")
		elif isAlignLeft(coldata[i]): print subVars("Tables","table-header-column-left")
		else:  print subVars("Tables","table-header-column")
	print subVars("Tables","after-table-header")

# handleTable()
# process a table and output a converted version of it
# input: globals
# output: standard out

def handleTable():

	global linePtr, level, exitlevel, v

	v["%%"] = lfStrip(semicolonStrip(lstrip(rstrip(lines[linePtr]))))

	if isFirstTableLine(linePtr):
		level = level + 1
		print subVars("Tables","before-table")
	if getTableType(linePtr) == "tableheader": 
		handleTableHeader()
	else: 
		handleTableRow()
	if isLastTableLine(linePtr): 
		print subVars("Tables","after-table")
		level = level - 1
		exitlevel = 1

# handlePrefText()
# process a block of body text and output a converted version of it
# input: globals
# output: standard out

def handlePrefText():

	global linePtr, lines, level, v, text

	v["%%"] = lfStrip(semicolonStrip(lstrip(rstrip(lines[linePtr]))))
	
	if isFirstPrefTextLine(linePtr):
		level = level + 1
		text = subVars("PrefText","before-preftext")
	if lstrip(rstrip(lines[linePtr])) == ";":
		text += subVars("PrefText","pref-paragraph-sep")
	else:
		text += subVars("PrefText","preftext")
	if isLastPrefTextLine(linePtr): 
		text += subVars("PrefText","after-preftext")
		print text
		text = ""
		level = level - 1
		exitlevel = 1

# handleUserText()
# process a block of user text and output a converted version of it
# input: globals
# output: standard out

def handleUserText():

	global linePtr, lines, level, v, text

	v["%%"] = lfStrip(greaterStrip(lstrip(rstrip(lines[linePtr],'\n'))))
	
	if isFirstUserTextLine(linePtr):
		level = level + 1
		text = subVars("UserText","before-user-text")
	if lstrip(rstrip(lines[linePtr])) == ">":
		text += subVars("UserText","user-paragraph-sep")
	else:
		text += subVars("UserText","user-text")
	if isLastUserTextLine(linePtr): 
		text += subVars("UserText","after-user-text")
		print text
		level = level - 1
		exitlevel = 1

# handleUserPrefText()
# process a block of body text and output a converted version of it
# input: globals
# output: standard out

def handleUserPrefText():

	global linePtr, lines, level, v, text

	v["%%"] = lfStrip(lessStrip(lstrip(rstrip(lines[linePtr]))))
	
	if isFirstPrefTextLine(linePtr):
		level = level + 1
		text = subVars("UserPrefText","before-user-preftext")
	if lstrip(rstrip(lines[linePtr])) == "<":
		text += subVars("UserPrefText","user-pref-paragraph-sep")
	else:
		text += subVars("UserPrefText","user-preftext")
	if isLastPrefTextLine(linePtr): 
		text += subVars("UserPrefText","after-user-preftext")
		print text
		level = level - 1
		exitlevel = 1

# addPreamble
# create the 'header' for the output document
# input: globals
# output: standard out

def addPreamble():
	global linePtr, lines, level, v

	v["%%"] = ""
	print subVars("Document","preamble")

# addPostamble
# create the 'header' for the output document
# input: globals
# output: standard out

def addPostamble():
	global linePtr, lines, level, v

	v["%%"] = ""
	print subVars("Document","postamble")

# handleObject
# process an object and print the converted line(s)
# input: linenum - current line pointer
# output: standard out

def handleObject(linenum):
	
	if getLineType(linenum) == 'heading': handleHeading()
	elif getLineType(linenum) == 'text': handleText()
	elif getLineType(linenum) == 'usertext': handleUserText()
	elif getLineType(linenum) == 'preftext': handlePrefText()
	elif getLineType(linenum) == 'userpreftext': handleUserPrefText()
	elif getLineType(linenum) == 'command': handleHeading()
	elif getLineType(linenum) == 'table': handleTable()
	else:
		print
		print "Error: unknown line type"
		sys.exit(1)

# handleObjects
# process a list of objects
# input: linenum - current line pointer
# output: standard out
# This is recursive. handleObject can call handleObjects.

def handleObjects():
	global lines, linePtr, level, exitlevel
	
	exitlevel = 0
	while (linePtr < len(lines)) and (exitlevel == 0):
		handleObject(linePtr)
		linePtr = linePtr + 1
	linePtr = linePtr - 1	# adjust for the unwanted post-increment
				# after the last line
	exitlevel = 0
	dprint("/ho")

###########################################################################
# Main Program Loop

def main():
	global inputfile, lines, debug, v, linePtr
	getArgs()
	if (debug !=0): printConfig()
	initVariables()
	readFile(inputfile)
	v["%t"] = lfStrip(lines[0])		# get the title
	linePtr = 1

	addPreamble()

	handleObjects()
		
	addPostamble()

main()
