#!/usr/bin/python
# encoding: utf-8
# author: Charles Joly Beauparlant
# 2013-04-23

"""
Usage:

generateXML.py [options] <filename1> <filename2> ... <filenameN>
	options: Optionnal parameter to modify the behavior of the script.
	    -p print only the filenames
"""

class XMLgenerator:
	def __init__(self, filenames, mode):
		self.m_filenames = filenames
		self.m_mode = mode
		self.m_values = []
		for i in range(0, len(self.m_filenames)):
			self.m_values.append(0)
		# If in "normal" mode, print xsl header and samples
		if self.m_mode == "-n":
			print '<?xml version="1.0" encoding="ISO-8859-1"?>'
			print '<?xml-stylesheet type="text/xsl" href="prototype.xsl"?>'
			print '<venn-analysis>'
			for i in range(0, len(self.m_filenames)):
				print '<sample>' + self.m_filenames[i] + '</sample>'

	def startAnalysis(self):
		self._recursiveAnnotation(0)		
		print '</venn-analysis>'

	def _print(self):
		allZeros = True
		for i in range(0, len(self.m_values)):
			if self.m_values[i] == 1:
				allZeros = False
		if allZeros == False:
			if self.m_mode == "-p":
				print self._convertValueToName() + ".txt"
			else:
				# Print name, id, path and count
				print '\t<value>'
				print '\t\t<name>' + self._convertValueToString() + '</name>'
				print '\t\t<id>' + self._createID() + '</id>'
				print '\t\t<path>lists/' + self._convertValueToName() + '.txt</path>'
				print '\t\t<count>' + self._fetchCount() + '</count>'
				print '\t</value>'

	def _createID(self):
		ID = ""
		count_1 = 0
		for i in range(0, len(self.m_values)):
			if self.m_values[i] == 1:
				count_1 += 1
		if count_1 == 1:
			ID += "Unique to "
		else:
			ID += "Common to "
		printCount = 0
		for i in range(0, len(self.m_values)):
			if self.m_values[i] == 1:
				ID += self.m_filenames[i]
				printCount += 1
				if printCount < count_1:
					if printCount == count_1 - 1:
						ID += " and "
					else:
						ID += ", "
		ID += "."
		return ID

	def _fetchCount(self):
		filename = "lists/" + self._convertValueToName() + ".txt"
		count = 0
		for line in open(filename):
			count += 1
		return str(count)
			
	def _convertValueToName(self):
		name = ""
		for i in range(0, len(self.m_values)):
			if self.m_values[i] == 1:
				name += self.m_filenames[i]
			else:
				name += "0"
			if i != len(self.m_values) - 1:
				name += "_"
		return name

	def _convertValueToString(self):
		name = ""
		for i in range(0, len(self.m_values)):
			if self.m_values[i] == 1:
				name += "1"
			else:
				name += "0"
			if i != len(self.m_values) - 1:
				name += "_"
		return name
				

	def _recursiveAnnotation(self, index):
		if index == len(filenames)-1:
			self.m_values[index] = 1
			self._print()
			self.m_values[index] = 0
			self._print()
		else:
			self.m_values[index] = 1
			index+=1
			self._recursiveAnnotation(index)
			self.m_values[index-1] = 0
			self._recursiveAnnotation(index)

import sys

if __name__=="__main__":
        if len(sys.argv) < 2:
                print __doc__
                sys.exit(1)

# Set the mode
mode = "-n"
if sys.argv[1] == "-p":
	mode = "-p"

# Load the files
filenames = []
fileCount = int(len(sys.argv)-1)
for i in range(0, fileCount):
	if mode != "-p" or i != 0:
		filenames.append(sys.argv[i+1])

xmlGenerator = XMLgenerator(filenames, mode)
xmlGenerator.startAnalysis()
