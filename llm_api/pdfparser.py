from py_pdf_parser.loaders import load_file
# from py_pdf_parser.visualise import visualise


document = load_file("18-spring-mid.pdf")
# visualise(document)

print(document.elements[4].text())