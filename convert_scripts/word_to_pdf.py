import os
import subprocess

def doc_to_pdf(input_dir, output_dir):
    if not os.path.exists(input_dir):
        print('Input directory not found!')
        return

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for file_name in os.listdir(input_dir):
        word_path = os.path.join(input_dir, file_name)

        try:
            subprocess.run(
                ["soffice", "--headless", "--convert-to", "pdf", word_path, "--outdir", output_dir],
                check=True
            )
            print(f"Conversion successful: {os.path.splitext(file_name)[0] + '.pdf'}")
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    input_path = '/home/veselin/w_t_pdf'
    output_path = '/home/veselin/w_t_pdf/pdfs'
    doc_to_pdf(input_path, output_path)
