import unittest
from MorseCodeGenerator import *

class CodeGeneratorTest(unittest.TestCase):

	def setUp(self):
		self.testText = "This is a test".upper()
		self.testMorse = "- .... .. ... / .. ... / .- / - . ... -"
		self.generator = MorseCodeGenerator()

	def test_construct(self):
		self.assertIsNotNone(self.generator)

	def test_generate_morse_from_text(self):
		self.assertEqual(self.generator.encode(self.testText), self.testMorse)

	def test_generate_text_from_morse(self):
		self.assertEqual(self.generator.decode(self.testMorse), self.testText)

	def test_string_too_short(self):
		self.assertFalse(self.generator.checkStringLength("a"))

	def test_string_too_long(self):
		self.assertFalse(self.generator.checkStringLength("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))

	def test_improper_symbols(self):
		self.assertFalse(self.generator.checkString("!@#$%^&*()+=`~,<>?[]{}|:;\_\""))

	def test_remove_improper_symbols(self):
		self.assertEqual(self.generator.cleanString("!@#$%^&*()_+=<>,;:'\"This is a test"), self.testText)


if __name__ == '__main__':
	unittest.main()