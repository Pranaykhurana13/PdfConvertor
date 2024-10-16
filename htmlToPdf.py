import pdfkit
from PyPDF2 import PdfWriter

path_to_wkhtmltopdf = '/usr/local/bin/wkhtmltopdf'
config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

options = {
    'page-size': 'A4',
    'orientation': 'Landscape',
    'zoom': 0.05
}

pdfkit.from_file('csv.html', 'csv.pdf', options=options, configuration=config)
pdfkit.from_file('json.html', 'json.pdf', options=options, configuration=config)

pdf_writer = PdfWriter()

for pdf_filename in ['csv.pdf', 'json.pdf']:
    with open(pdf_filename, 'rb') as pdf_file:
        pdf_writer.append(pdf_file)

with open('output.pdf', 'wb') as output_pdf_file:
    pdf_writer.write(output_pdf_file)
