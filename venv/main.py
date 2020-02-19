import PyPDF2

# with open('./docs/dummy.pdf', 'rb') as file:
#     reader = PyPDF2.PdfFileReader(file)
#     # print(reader.numPages)
#     # print(reader.getPage(0))
#     page = reader.getPage(0)
#
#     # page.rotatecounterClockwise(90)
#
#     writer = PyPDF2.PdfFileWriter
#     writer.addPage(page)
#     with open('./docs/tilt.pdf', 'wb') as new_file:
#         writer.write(new_file)

# w/ watermark
template = PyPDF2.PdfFileReader(open('./docs/super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('./docs/wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
  page = template.getPage(i)
  page.mergePage(watermark.getPage(0))
  output.addPage(page)

  with open('./docs/watermarked_output.pdf', 'wb') as file:
    output.write(file)