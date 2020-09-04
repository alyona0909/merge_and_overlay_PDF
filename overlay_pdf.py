import PyPDF2
import sys, os, re

# function to check is input valid
def check_input(pdf):
	valid_pattern = re.compile(r"[a-zA-Z0-9\,\.\-\/_:]{1,}\.pdf")
	return valid_pattern.fullmatch(pdf)

# function to overlay a pdf file with a watermark on another one
def mk_wtrmark(pdf, wtr):
	try:
		if not check_input(pdf):
			raise Exception(f"Wrong name of file : {pdf}")
		if not check_input(wtr):
			raise Exception(f"Wrong name of file : {wtr}")
		if not os.path.exists(pdf):
			raise Exception(f"File : {pdf} doesn\'t exists")
		if not os.path.exists(wtr):
			raise Exception(f"File : {wtr} doesn\'t exists")

		reader = PyPDF2.PdfFileReader(open(pdf, 'rb'))
		writer = PyPDF2.PdfFileWriter()
		watermark = PyPDF2.PdfFileReader(open(wtr, 'rb'))

		# on every page of reader overlay a watermark page
		for i in range(reader.numPages):
 			page = reader.getPage(i)
 			page.mergePage(watermark.getPage(0))
 			writer.addPage(page)
 		
		with open('result_with_wtr.pdf', 'wb') as file:
			writer.write(file)
		return 0
	except Exception as err:
		print(err)
		return str(err)

if __name__ == '__main__':
	pdf = sys.argv[1]
	wtr = sys.argv[2]
	mk_wtrmark(pdf, wtr)
