import os
from pdf2docx import Converter

def pdf_to_doc(input_dir, output_dir):
    if not os.path.exists(input_dir):
        print('Directory not found')
        return

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for file_name in os.listdir(input_dir):
        if file_name.lower().endswith('.pdf'):
            pdf_path = os.path.join(input_dir, file_name)
            docx_filename = os.path.splitext(file_name)[0] + '.docx'
            docx_file_path = os.path.join(output_dir, docx_filename)

            try:
                cv = Converter(pdf_path)
                cv.convert(docx_file_path, start=0, end=None)
                cv.close()
                print('Conversion successful')
            except Exception as e:
                print(f"Error: {e}")

if __name__ == '__main__':
    input_path = '/home/veselin/pdf_t_w'
    output_path = '/home/veselin/pdf_t_w/docs'
    pdf_to_doc(input_path, output_path)

