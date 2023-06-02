import aspose.words as aw

def pdf_to_docx(pdf_path, docx_path):
    # Load the PDF document
    pdf_document = aw.Document(pdf_path)

    # Save the PDF document as DOCX
    pdf_document.save(docx_path, aw.SaveFormat.DOCX)

import pathlib
pdf_path = str(pathlib.Path(__file__).parent.resolve()) +'\\1.pdf'
docx_path = str(pathlib.Path(__file__).parent.resolve()) +'\\1.docx'

pdf_to_docx(pdf_path, docx_path)
