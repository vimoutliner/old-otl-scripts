#!/usr/bin/python
# otl2html.py
# convert a tab-formatted outline from VIM to HTML
#
# Copyright 2001 Noel Henson All rights reserved
#
# ALPHA VERSION!!!
# $Revision: 1.29 $
# $Date: 2004/11/28 17:31:34 $
# $Author: noel $
# $Source: /home/noel/active/NoelOTL/RCS/otl2html.py,v $
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
from re import *
from time import *

###########################################################################
# global variables

formatMode = "simple"
copyright = ""
level = 0
div = 0
slides = 0
hideComments = 0
inputFile = ""
outline = []
flatoutline = []
inBodyText = 0		# 0: no, 1: text, 2: preformatted text, 3: table
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
   print "    -p              Presentation: slide show output for use with HtmlSlides."
   print "    -D              First-level is divisions (<div> </div>) for making"
   print "                    pretty web pages."
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
   print " $Revision: 1.29 $"
   print " $Date: 2004/11/28 17:31:34 $"
   print " $Author: noel $"
   print " $Source: /home/noel/active/NoelOTL/RCS/otl2html.py,v $"
   print

# getArgs
# Check for input arguments and set the necessary switches
# input: none
# output: possible console output for help, switch variables may be set

def getArgs():
  global inputfile, debug, formatMode, slides, hideComments, copyright, styleSheet, inlineStyle, div
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
        elif (sys.argv[i] == "-D"):		# test for the divisions flag
	  div = 1				# set the divisions flag
        elif (sys.argv[i] == "-c"):		# test for the comments flag
	  hideComments = 1			# set the comments flag
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

# semicolonStrip(line)
# stip a leading ';', if it exists
# input: line
# output: returns a string with a stipped ';'

def semicolonStrip(line):
	if (line[0] == ";"): return line[1:]
        else: return line

# dashStrip(line)
# stip a leading '-', if it exists
# input: line
# output: returns a string with a stipped '-'

def dashStrip(line):
	if (line[0] == "-"): return line[1:]
        else: return line

# pipeStrip(line)
# stip a leading '|', if it exists
# input: line
# output: returns a string with a stipped '|'

def pipeStrip(line):
	if (line[0] == "|"): return line[1:]
        else: return line

# plusStrip(line)
# stip a leading '+', if it exists
# input: line
# output: returns a string with a stipped '+'

def plusStrip(line):
	if (line[0] == "+"): return line[1:]
        else: return line

# handleBodyText
# print body text lines with a class indicating level, if style sheets
# are being used. otherwise print just <p>
# input: linein - a single line that may or may not have tabs at the beginning
# output: through standard out

def handleBodyText(linein,lineLevel):
  global inBodyText
  print "<p",
  if (styleSheet != ""):
    print " class=\"P" + str(lineLevel) + "\"",
    inBodyText = 1
  print ">" + colonStrip(rstrip(lstrip(linein))),

# handlePreformattedText
# print preformatted text lines with a class indicating level, if style sheets
# are being used. otherwise print just <pre>
# input: linein - a single line that may or may not have tabs at the beginning
# output: through standard out

def handlePreformattedText(linein,lineLevel):
  global inBodyText
  print "<pre",
  if (styleSheet != ""):
    print " class=\"PRE" + str(lineLevel) + "\"",
    inBodyText = 2
  print ">" + semicolonStrip(rstrip(lstrip(linein))),


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

# getColumnAlignment(string)
# return string
# input: coldata
# output: <td align="left"> or <td align="right"> or <td align="center"> or <td>

def getColumnAlignment(coldata):
	if isAlignCenter(coldata): return '<td align="center">'
	if isAlignRight(coldata): return '<td align="right">'
	if isAlignLeft(coldata): return '<td align="left">'
	return '<td>'

# handleTableColumns
# return the souce for a row's columns
# input: linein - a single line that may or may not have tabs at the beginning
# output: string with the columns' source

def handleTableColumns(linein,lineLevel):
  out = ""
  coldata = lstrip(rstrip(linein))
  coldata = split(coldata,"|")
  for i in range(1,len(coldata)-1):
		out += getColumnAlignment(coldata[i])
		out += lstrip(rstrip(coldata[i]))+'</td>'
  return out 

# handleTableHeaders
# return the souce for a row's headers
# input: linein - a single line that may or may not have tabs at the beginning
# output: string with the columns' source

def handleTableHeaders(linein,lineLevel):
  out = ""
  coldata = lstrip(rstrip(linein))
  coldata = split(coldata,"|")
  for i in range(2,len(coldata)-1):
		out += getColumnAlignment(coldata[i])
		out += lstrip(rstrip(coldata[i]))+'</td>'
  out = replace(out,'<td','<th')
  out = replace(out,'</td','</th')
  return out 

# handleTableRow
# print a table row
# input: linein - a single line that may or may not have tabs at the beginning
# output: out

def handleTableRow(linein,lineLevel):
  out = "<tr>"
  if (lineLevel == find(linein,"|| ") +1 ): 
         out += handleTableHeaders(linein,lineLevel)
  else:  out += handleTableColumns(linein,lineLevel)
  out += "</tr>"
  return out

# handleTable
# print a table, starting with a <TABLE> tag if necessary
# input: linein - a single line that may or may not have tabs at the beginning
# output: through standard out

def handleTable(linein,lineLevel):
  global inBodyText
  if (inBodyText != 3): 
	  print "<table class=\"TAB" + str(lineLevel) + "\">"
	  inBodyText = 3
  print handleTableRow(linein,lineLevel), 

# linkOrImage
# if there is a link to an image or another page, process it
# input: line
# output: modified line

def linkOrImage(line):
  line = sub('\[(\S+?)\]','<img src="\\1">',line)
  line = sub('\[(\S+)\s(.*?)\]','<a href="\\1">\\2</a>',line)
  line = replace(line,'<img src="X">','[X]')
  line = replace(line,'<img src="_">','[_]')
  return line

# divName
# create a name for a division
# input: line
# output: division name
def divName(line):
	line = lstrip(rstrip(line))
	line = replace(line, ' ', '_')
	return'<div class="' + line + '">'

def beautifyLine(line):
  if (lstrip(rstrip(line)) == "----------------------------------------"):
        return "<br><hr><br>"
  
  out = line
  line = ""

  while (line != out):

	  line = out
	  out = linkOrImage(out)
	# out = replace(out,'**','<strong>',1)
	  out = sub('\*\*(.*?)\*\*','<strong>\\1</strong>',out)
	# out = replace(out,'//','<i>',1)
	  out = sub('\/\/(.*?)\/\/','<i>\\1</i>',out)
	# out = replace(out,'+++','<code>',1)
	  out = sub('\+\+\+(.*?)\+\+\+','<code>\\1</code>',out)
	# out = replace(out,'---','<strike>',1)
	  out = sub('\-\-\-(.*?)\-\-\-','<strike>\\1</strike>',out)
  return out

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
  global level, formatMode, slides, hideComments, inBodyText, styleSheet, inlineStyle, div
  if (lstrip(linein) == ""): return
  linein = beautifyLine(linein)
  lineLevel = getLineLevel(linein)
  if ((hideComments == 0) or (lineLevel != (find(linein,"[")+1))):

      if (lineLevel > level): # increasing depth
       while (lineLevel > level):
    	if (formatMode == "indent"):
          if (inBodyText == 1):
	    print"</p>"
	    inBodyText = 0
    	  print "<ol>"
    	else:
    	  sys.exit("Error! Unknown formatMode type")
    	level = level + 1

      elif (lineLevel < level): # decreasing depth
       while (lineLevel < level):
        if (inBodyText == 1):
	  print"</p>"
	  inBodyText = 0
        elif (inBodyText == 2):
	  print"</pre>"
	  inBodyText = 0
        elif (inBodyText == 3):
	  print"</table>"
	  inBodyText = 0
  	print "</ol>"
  	level = level - 1
	if (div == 1 and level == 1): print'</div>'

      else: print # same depth

      if (slides == 0):
          if (lineLevel == find(linein," ") +1 ) or \
	  (lineLevel == find(linein,":") +1 ): 
		  if (inBodyText == 0): handleBodyText(linein,lineLevel)
		  elif (colonStrip(rstrip(lstrip(linein))) == ""):
			  print "</p>"
			  handleBodyText(linein,lineLevel)
            	  else: print colonStrip(rstrip(lstrip(linein))),
          elif (lineLevel == find(linein,";") +1 ): 
		  if (inBodyText == 0): handlePreformattedText(linein,lineLevel)
		  elif (semicolonStrip(rstrip(lstrip(linein))) == ""):
			  print "</pre>"
			  handlePreformattedText(linein,lineLevel)
            	  else: print semicolonStrip(rstrip(lstrip(linein))),
          elif (lineLevel == find(linein,"|") +1 ): 
		  if (inBodyText == 0): handleTable(linein,lineLevel)
		  elif (pipeStrip(rstrip(lstrip(linein))) == ""):
			  print "</table>"
			  handleTtable(linein,lineLevel)
            	  else: print handleTableRow(linein,lineLevel),
  	  else:
            if (inBodyText == 1):
	    	    print"</p>"
		    inBodyText = 0
            elif (inBodyText == 2):
	    	    print"</pre>"
		    inBodyText = 0
            elif (inBodyText == 3):
	    	    print"</table>"
		    inBodyText = 0
	    if (div == 1 and lineLevel == 1): print divName(linein)
            print "<li",
	    if (styleSheet != ""):
	      if (lineLevel == find(linein,"- ") +1 ): 
                print " class=\"LB" + str(lineLevel) + "\"",
                print ">" + lstrip(rstrip(dashStrip(lstrip(linein)))),
	      elif (lineLevel == find(linein,"+ ") +1 ): 
                print " class=\"LN" + str(lineLevel) + "\"",
                print ">" + lstrip(rstrip(plusStrip(lstrip(linein)))),
	      else:
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
              print "<li",
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
  global styleSheet, inlineStyle
  print "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01//EN\" \"http://www.w3.org/TR/html4/strict.dtd\">"
  print "<html><head><title>" + linein + "</title>"
  print"<!--  $Revision: 1.29 $ -->"
  print"<!--  $Date: 2004/11/28 17:31:34 $ -->"
  print"<!--  $Author: noel $ -->"
  file = open(styleSheet,"r")
  if (styleSheet != "" and inlineStyle == 0):
    print "<link href=\"" + styleSheet + "\" rel=\"stylesheet\" type=\"text/css\">"
  if (styleSheet != "" and inlineStyle == 1):
    print "<style type=\"text/css\">"
    csslinein = file.readline()
    while csslinein != "":
      print csslinein,
      csslinein = file.readline()
    file.close()
    print "</style></head>"
  print "<body>"
  print "<div class=\"DocTitle\">"
  print "<h1>" + rstrip(lstrip(linein)) +"</h1>"
  print "</div>"
  print "<div class=\"MainPage\">"

def printFooter():
  global slides, div
  print "</div>"
  if (slides == 0 and div == 0):
          print "<div class=\"Footer\">"
	  print "<hr>"
	  print copyright
	  print "<br>"
	  print inputfile + "&nbsp&nbsp " + strftime("%Y/%m/%d %H:%M",localtime(time()))
          print "</div>"
  print "</body></html>"

def main():
  getArgs()
  flatouline = []
  file = open(inputfile,"r")
  if (slides == 0):
    firstLine = beautifyLine(lstrip(rstrip(file.readline())))
    printHeader(firstLine)
    linein = beautifyLine(lstrip(rstrip(file.readline())))
    while linein != "":
      processLine(linein)
      linein = file.readline()
    closeLevels()
  else:
    linein = beautifyLine(lstrip(rstrip(file.readline())))
    outline.append(linein)
    linein = lstrip(rstrip(file.readline()))
    while linein != "":
      outline.append("\t" + linein)
      linein = rstrip(file.readline())
    for i in range (0,len(outline)-1):
      flatten(i)
    printHeader(flatoutline[0])
    for i in range (0,len(flatoutline)):
      processLine(flatoutline[i])
    
  printFooter()
  file.close()

main()
    
