# merge_and_overlay_PDF
> A console  application for combining multiple pdf files into one and for applying watermarks to a file

## Getting Started
Before using you need to install :

```sh
pip install PyPDF2
```

## Combining

Use combine_pdf.py for combining files : you can enter the required number of paths to PDF files in the console and launch it.

### For example input in console : 

```sh
python combine_pdf.py testing/examples/dummy.pdf testing/examples/twopage.pdf testing/examples/wtr.pdf
```

## Overlaying

Use overlay_pdf.py for applying watermarks : you can enter the path to the file to apply the watermark to and the path to the file with the watermark in the console and launch it.

### For example input in console : 

```sh
python overlay_pdf.py testing/examples/result.pdf testing/examples/wtr.pdf 
```
## Examples
There are a few examples and tests in folder /testing/.
