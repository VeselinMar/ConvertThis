import os
from pdf2docx import Converter

def pdf_to_word(pdf_path, word_path=None):
    if not os.path.exists(pdf_path):
        print('File not found')
        return

    if word_path is None:
        word_path = os.path.splitext(pdf_path)[0] + '.docx'

    try:
        cv = Converter(pdf_path)
        cv.convert(word_path, start=0, end=None)
        cv.close()
        print('Conversion successful')
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    pdf_path = input('PDF path:')
    pdf_to_word(pdf_path)

