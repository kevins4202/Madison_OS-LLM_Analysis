from py_pdf import PdfReader

reader = PdfReader("18-spring-mid.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
print(page)
text = page.extract_text()
# print(text)