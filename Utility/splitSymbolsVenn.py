#!/usr/bin/python
# encoding: utf-8
# author: Charles Joly Beauparlant
# 2013-04-05

"""
This script splits gene symbols from multiple files for Venn diagram.
Will only save one of the possible combination of samples to make it easier to include in a Makefile pipeline.

Usage:
./splitSymbolVenn.py <outputFile> <inputFile1> ... <inputFileN> 
	outputFile: The combination of samples to save. (i.e.: IRF7-0-0)."
		    Note that the order of the combination must match the order of the filenames.
	inputFiles: List of file to analyse
"""

class VennParser:
	def __init__(self, filenames):
		self.m_fileCount = len(filenames)
		self.m_fileList = filenames
		self.m_symbolList = {}
		self.m_filenames = []
		for i in range(0, self.m_fileCount):
			self.m_filenames.append(self.m_fileList[i].split("/")[len(self.m_fileList[i].split("/")) - 1])

	def parseFiles(self):
		for filename in self.m_fileList:
			self._parseFile(filename)

	def printCombination(self, combination):
		self._checkCombination(combination)
		if len(self.m_fileList) > self.m_fileCount - 1:
			for symbol in self.m_symbolList:
				if self.m_symbolList[symbol] == self._convertCombinationToValue(combination):
					print symbol

	def _parseFile(self, filename):
		currentFilenameColorValue = self._convertFilenameToColorValue(filename)
		for line in open(filename):
			symbol = line.strip()
			self._addSymbol(symbol, currentFilenameColorValue)

	def _checkCombination(self, combination):
		combinations = combination.split("_")
		if len(combinations) != len(self.m_filenames):
			sys.exit("Error! The number of element in combination (" + combination + ") and the number of files does not match.")
		for i in range(0, len(combinations)):
			if combinations[i] != "0" and combinations[i] not in self.m_filenames:
				sys.exit("Error! Combination \"" + combinations[i] + "\" does not match any of the filenames")

	def _convertCombinationToValue(self, combination):
		combinations = combination.split("_")
		toReturn = 0
		for i in range(0, len(combinations)):
			if combinations[i] != "0":
				completeFilename = self._fetchCompleteFilename(combinations[i])
				colorValue = self._convertFilenameToColorValue(completeFilename)
				toReturn = self._updateVirtualColor(colorValue, toReturn)
		return toReturn

	def _fetchCompleteFilename(self, filename):
		for i in range(0, len(self.m_filenames)):
			if filename == self.m_fileList[i].split("/")[len(self.m_fileList[i].split("/"))-1]:
				return self.m_fileList[i]
		sys.exit("_fetchCompleteFilename: Error! " + filename + " not in file list")

	def _convertFilenameToColorValue(self, filename):
		filename_index = self.m_fileList.index(filename)
		return 10**filename_index

	def _addSymbol(self, symbol, colorValue):
		if symbol in self.m_symbolList:
			lastColorValue = self.m_symbolList[symbol]
			self.m_symbolList[symbol] = self._updateVirtualColor(colorValue, lastColorValue)
		else:
			self.m_symbolList[symbol] = colorValue

	def _updateVirtualColor(self, filenameColorValue, lastColorValue = 0):
		newValue = lastColorValue
		if filenameColorValue != 0:
			if ((lastColorValue / filenameColorValue) % 2) == 0:
				newValue = lastColorValue + filenameColorValue
		return newValue

import sys

if __name__=="__main__":
        if len(sys.argv) < 2:
                print __doc__
                sys.exit(1)

# Fetch the filenames
filenames = []
fileCount = int(len(sys.argv)-1)
for i in range(1, fileCount):
	filenames.append(sys.argv[i+1])

combination = sys.argv[1]
	
vennParser = VennParser(filenames)
vennParser.parseFiles()
vennParser.printCombination(combination)
