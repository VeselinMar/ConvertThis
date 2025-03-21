import os
import subprocess

def word_to_pdf(word_path, pdf_path=None):
    if not os.path.exists(word_path):
        print('File not found')
        return

    if pdf_path is None:
        pdf_path = os.path.splitext(word_path)[0] + '.pdf'

    try:
        subprocess.run(
            ["soffice", "--headless", "--convert-to", "pdf", word_path, "--outdir", os.path.dirname(pdf_path)],
            check=True
        )
        print(f"Conversion successful: {pdf_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    word_path = input('Word path:')
    word_to_pdf(word_path)
