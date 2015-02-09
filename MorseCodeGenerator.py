class MorseCodeGenerator:
	def __init__ (self):
		self.library = {"a" : ".-",
						"b" : "-...",
						"c" : "-.-.",
						"d" : "-..",
						"e" : ".",
						"f" : "..-.",
						"g" : "--.",
						"h" : "....",
						"i" : "..",
						"j" : ".---",
						"k" : "-.-",
						"l" : ".-..",
						"m" : "--",
						"n" : "-.",
						"o" : "---",
						"p" : ".--.",
						"q" : "--.-",
						"r" : ".-.",
						"s" : "...",
						"t" : "-",
						"u" : "..-",
						"v" : "...-",
						"w" : "...-",
						"x" : "_.._",
						"y" : "-.--",
						"z" : "--..",
						"A" : ".-",
						"B" : "-...",
						"C" : "-.-.",
						"D" : "-..",
						"E" : ".",
						"F" : "..-.",
						"G" : "--.",
						"H" : "....",
						"I" : "..",
						"J" : ".---",
						"K" : "-.-",
						"L" : ".-..",
						"M" : "--",
						"N" : "-.",
						"O" : "---",
						"P" : ".--.",
						"Q" : "--.-",
						"R" : ".-.",
						"S" : "...",
						"T" : "-",
						"U" : "..-",
						"V" : "...-",
						"W" : "...-",
						"X" : "_.._",
						"Y" : "-.--",
						"Z" : "--..",
						"1" : ".----",
						"2" : "..---",
						"3" : "...--",
						"4" : "....-",
						"5" : ".....",
						"6" : "-....",
						"7" : "--...",
						"8" : "---..",
						"9" : "----.",
						"0" : "-----",
						" " : "/"
						}

	def encode(self, string):
		cipher = ""
		if(not(self.checkStringLength(string))):
			for x in xrange(0,len(string)):
				if x == len(string) - 1:
					cipher += self.library[string[x]]
				else:
					cipher += self.library[string[x]] + " "
		return cipher

	def decode(self, string):
		codeStrings = string.split();
		plainText = ""
		for x in codeStrings:
			for character, code in self.library.items():
				if(x == code):
					plainText += character
		return plainText

	def checkStringLength(self, string):
		if(len(string) >= 3  or len(string) <= 42):
			return False
		return True

	def checkString(self, string):
		return True

	def cleanString(self, string):
		return string
