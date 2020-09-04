import PyPDF2
import sys, os, re

# function to check is input valid
def check_input(pdf):
	valid_pattern = re.compile(r"[a-zA-Z0-9\,\.\-\/_:]{1,}\.pdf")
	return valid_pattern.fullmatch(pdf)

# function to merge pdf files into one
def pdf_combiner(pdf_list):
	try:
		if len(pdf_list) < 2:
			raise Exception("Please enter more then one file name")
		merger = PyPDF2.PdfFileMerger()
		for name in pdf_list:
			if not check_input(name):
				raise Exception(f"Wrong name of file : {name}")
			if not os.path.exists(name):
				raise Exception(f"File : {name} doesn\'t exists")
			merger.append(name)
		merger.write('result.pdf')
		return 0
	except Exception as err:
		print(err)
		return str(err)

if __name__ == '__main__':
	name_files = sys.argv[1:]
	pdf_combiner(name_files)
