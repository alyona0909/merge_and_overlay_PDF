import unittest
import sys
sys.path.append('../')
from overlay_pdf import mk_wtrmark

class TestMain(unittest.TestCase):
	def test_combine(self):
		file1 = "examples/dummy.pdf"
		file2 = "examples/wtr.pdf"
		res = mk_wtrmark(file1, file2)
		self.assertEqual(res, 0)

	def test_combine_name_files(self):
		file1 = "examples/dummy"
		file2 = "examples/wtr.pdf"
		res = mk_wtrmark(file1, file2)
		self.assertEqual(res, "Wrong name of file : examples/dummy")

	def test_combine_name_files2(self):
		file1 = "examples/dummy1.pdf"
		file2 = "examples/wtr.pdf"
		res = mk_wtrmark(file1, file2)
		self.assertEqual(res, "File : examples/dummy1.pdf doesn\'t exists")

if __name__ == '__main__':
		unittest.main()	