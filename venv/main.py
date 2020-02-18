import PyPDF2

with open('./docs/dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    # print(reader.numPages)
    # print(reader.getPage(0))
    page = reader.getPage(0)

    # page.rotatecounterClockwise(90)

    writer = PyPDF2.PdfFileWriter
    writer.addPage(page)
    with open('./docs/tilt.pdf', 'wb') as new_file:
        writer.write(new_file)