import unittest
import sys
sys.path.append('../')
from combine_pdf import pdf_combiner

class TestMain(unittest.TestCase):
	def test_combine(self):
		file1 = "examples/dummy.pdf"
		file2 = "examples/twopage.pdf"
		file3 = "examples/wtr.pdf"
		res = pdf_combiner([file1, file2, file3])
		self.assertEqual(res, 0)

	def test_combine_name_files(self):
		file1 = "examples/dummy.pdf"
		file2 = "examples/twopage"
		file3 = "examples/wtr.pdf"
		res = pdf_combiner([file1, file2, file3])
		self.assertEqual(res, "Wrong name of file : examples/twopage")

	def test_combine_name_files2(self):
		file1 = "examples/dummy1.pdf"
		file2 = "examples/wtr.pdf"
		res = pdf_combiner([file1, file2])
		self.assertEqual(res, "File : examples/dummy1.pdf doesn\'t exists")

	def test_combine_less_files(self):
		file1 = "examples/dummy.pdf"
		res = pdf_combiner([file1])
		self.assertEqual(res, "Please enter more then one file name")

if __name__ == '__main__':
		unittest.main()	