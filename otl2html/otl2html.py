#!/usr/bin/python
# otl2html.py
# convert a tab-formatted outline from VIM to HTML
#
# Copyright 2001 Noel Henson All rights reserved
#
# ALPHA VERSION!!!
# $Revision: 1.16 $
# $Date: 2003/11/23 01:01:48 $
# $Author: noel $
# $Source: /home/noel/apps/NoelOTL/RCS/otl2html.py,v $
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
#	CSS support has been added.
#


###########################################################################
# include whatever mdules we need

import sys
from string import *
from time import *

###########################################################################
# global variables

formatMode = "simple"
copyright = ""
level = 0
slides = 0
hideComments = 0
inputFile = ""
outline = []
flatoutline = []
inBodyText = 0
styleSheet = ""
inlineStyle = 0

###########################################################################
# function definitions

# usage
# print the simplest form of help
# input: none
# output: simple command usage is printed on the console
 
def showUsage():
   print
   print "Usage:"
   print "otl2html.py [options] inputfile > outputfile"
   print "Options"
   print "    -t type        Specify the format type."
   print "                   Types:"
   print "                      simple - uses HTML tags <H1> through <H9>"
   print "                      bullets - uses HTML tags <UL> and <LI>"
   print "                      numeric - uses HTML tags <OL> and <LI> for 1.1.1"
   print "                      roman - uses HTML tags <OL> and <LI> for I.I.I"
   print "                      alpha - uses HTML tags <OL> and <LI> for A.A.A"
   print "                      indent - uses HTML tags <OL> and <LI>"
   print "                      Not compatible with -s or -S."
   print "    -p              Presentation: slide show output for use with HtmlSlides."
   print "    -s sheet        Use the specified style sheet with a link. Not compatible"
   print "                    with -t."
   print "    -S sheet        Include the specified style sheet in-line the output. For"
   print "                    encapsulated style. Not compatible with -t. Hide"
   print "    -c              comments (line with [ as the first non-whitespace"
   print "                    character. Ending with ] is optional."
   print "    -C copyright    Override the internal copyright notice with the"
   print "                    one supplied in the quoted string following this"
   print "                    flag. Single or double quotes can be used."
   print "    -v              Print version (RCS) information."
   print "output is on STDOUT"
   print

# version
# print the RCS version information
# input: none
# output: RSC version information is printed on the console
 
def showVersion():
   print
   print "RCS"
   print " $Revision: 1.16 $"
   print " $Date: 2003/11/23 01:01:48 $"
   print " $Author: noel $"
   print " $Source: /home/noel/apps/NoelOTL/RCS/otl2html.py,v $"
   print

# getArgs
# Check for input arguments and set the necessary switches
# input: none
# output: possible console output for help, switch variables may be set

def getArgs():
  global inputfile, debug, formatMode, slides, hideComments, copyright, styleSheet, inlineStyle
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
        elif (sys.argv[i] == "-p"):		# test for the slides flag
	  slides = 1				# set the slides flag
        elif (sys.argv[i] == "-c"):		# test for the comments flag
	  hideComments = 1			# set the comments flag
        elif (sys.argv[i] == "-t"):		# test for the type flag
	  formatMode = sys.argv[i+1]		# get the type
	  i = i + 1				# increment the pointer
        elif (sys.argv[i] == "-C"):		# test for the copyright flag
	  copyright = sys.argv[i+1]		# get the copyright
	  i = i + 1				# increment the pointer
        elif (sys.argv[i] == "-s"):		# test for the style sheet flag
	  styleSheet = sys.argv[i+1]		# get the style sheet name
	  formatMode = "indent"			# set the format
	  i = i + 1				# increment the pointer
        elif (sys.argv[i] == "-S"):		# test for the style sheet flag
	  styleSheet = sys.argv[i+1]		# get the style sheet name
	  formatMode = "indent"			# set the format
	  inlineStyle = 1
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
    
# colonStrip(line)
# stip a leading ':', if it exists
# input: line
# output: returns a string with a stipped ':'

def colonStrip(line):
	if (line[0] == ":"): return lstrip(line[1:])
        else: return line

# handleBodyText
# print body text lines with a class indicating level, if style sheets
# are being used. otherwise print just <P>
# input: linein - a single line that may or may not have tabs at the beginning
# output: through standard out

def handleBodyText(linein,lineLevel):
  global inBodyText
  print "<P",
  if (styleSheet != ""):
    print " class=\"P" + str(lineLevel) + "\"",
    inBodyText = 1
  print ">" + colonStrip(rstrip(lstrip(linein))),

# closeLevels
# generate the number of </ul> or </ol> tags necessary to proplerly finish
# input: format - a string indicating the mode to use for formatting
#        level - an integer between 1 and 9 that show the current level
# 	          (not to be confused with the level of the current line)
# output: through standard out

def closeLevels():
  global level, formatMode
  while (level > 0):
    if (formatMode == "bullets"):
      print "</ul>"
    if (formatMode == "alpha") or (formatMode == "numeric") or \
    (formatMode == "roman") or (formatMode == "indent"):
      print "</ol>"

    level = level - 1


# processLine
# process a single line
# input: linein - a single line that may or may not have tabs at the beginning
#        format - a string indicating the mode to use for formatting
#        level - an integer between 1 and 9 that show the current level
# 	          (not to be confused with the level of the current line)
# output: through standard out

def processLine(linein):
  global level, formatMode, slides, hideComments, inBodyText, styleSheet, inlineStyle
  if (lstrip(linein) == ""): return
  lineLevel = getLineLevel(linein)
  if ((hideComments == 0) or (lineLevel != (find(linein,"[")+1))):
    if (formatMode == "simple"):
      print "<H" + str(lineLevel) + ">" + lstrip(linein) + "</H" + str(lineLevel) + ">"
    else:
      if (lineLevel > level):
       while (lineLevel > level):
    	if (formatMode == "bullets"):
          if (inBodyText == 1):
	    print"</p>"
	    inBodyText = 0
    	  print "<UL>"
    	elif (formatMode == "roman"):
          if (inBodyText == 1):
	    print"</p>"
	    inBodyText = 0
    	  print "<OL type=\"I\">"
    	elif (formatMode == "numeric"):
          if (inBodyText == 1):
	    print"</p>"
	    inBodyText = 0
    	  print "<OL type=\"1\">"
    	elif (formatMode == "alpha"):
          if (inBodyText == 1):
	    print"</p>"
	    inBodyText = 0
    	  print "<OL type=\"A\">"
    	elif (formatMode == "indent"):
          if (inBodyText == 1):
	    print"</p>"
	    inBodyText = 0
    	  print "<OL>"
    	else:
    	  sys.exit("Error! Unknown formatMode type")
    	level = level + 1
      elif (lineLevel < level):
       while (lineLevel < level):
  	if (formatMode == "bullets"):
          if (inBodyText == 1):
	    print"</p>"
	    inBodyText = 0
  	  print "</UL>"
  	else:
          if (inBodyText == 1):
	    print"</p>"
	    inBodyText = 0
  	  print "</OL>"
  	level = level - 1
      else:
        print
      if (lstrip(rstrip(linein)) == "----------------------------------------"):
        print "<br><br><hr><br>"
      else:
        if (slides == 0):
          if (lineLevel == find(linein," ") +1 ) or \
	  (lineLevel == find(linein,":") +1 ): 
		  if (inBodyText == 0): handleBodyText(linein,lineLevel)
            	  else: print colonStrip(rstrip(lstrip(linein))),
  	  else:
            if (inBodyText == 1):
	    	    print"</p>"
		    inBodyText = 0
            print "<LI",
	    if (styleSheet != ""):
              print " class=\"L" + str(lineLevel) + "\"",
            print ">" + rstrip(lstrip(linein)),
        else:
          if (lineLevel == 1):
            if (linein[0] == " "):
	      if (inBodyText == 0):
		handleBodyText(linein,lineLevel)
	      else: print rstrip(lstrip(linein)),
            else:
              print "<address>"
	      print rstrip(lstrip(linein)),
	      print "</address>\n"
          else:
	    if (lineLevel == find(linein," ") +1 ) or \
	    (lineLevel == find(linein,":") +1 ): 
		    if (inBodyText == 0):
		        handleBodyText(linein,lineLevel)
	      	    else: print rstrip(lstrip(linein)),
            else:
              if (inBodyText == 1):
	    	    print"</p>"
		    inBodyText = 0
              print "<LI",
	      if (styleSheet != ""):
                print " class=\"LI.L" + str(lineLevel) + "\"",
              print ">" + rstrip(lstrip(linein)),
      
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
  print "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01//EN\" \"http://www.w3.org/TR/html4/strict.dtd\">"
  print "<HTML><TITLE>" + linein + "</TITLE>"
  print"<!--  $Revision: 1.16 $ -->"
  print"<!--  $Date: 2003/11/23 01:01:48 $ -->"
  print"<!--  $Author: noel $ -->"

def printStyle(linein):
  global styleSheet, inlineStyle
  file = open(styleSheet,"r")
  if (styleSheet != "" and inlineStyle == 0):
    print "<HEAD><LINK href=\"" + styleSheet + "\" rel=\"stylesheet\" type=\"text/css\"></HEAD>"
  if (styleSheet != "" and inlineStyle == 1):
    print "<HEAD><STYLE type=\"text/css\">"
    csslinein = file.readline()
    while csslinein != "":
      print csslinein,
      csslinein = file.readline()
    file.close()
    print "</STYLE></HEAD>"
  print "<BODY>"
  print "<DIV TITLE=\"DocTitle\">"
  print "<H1>" + rstrip(lstrip(linein)) +"</H1>"
  print "</DIV>"
  print "<DIV TITLE=\"Main\">"

def printFooter():
  global slides
  print "</DIV>"
  if (slides == 0):
	  print "<hr><font size=1>"
	  print copyright
	  print "</font><br>"
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
    closeLevels()
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
    
