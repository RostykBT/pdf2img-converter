import os
from pdf2image import convert_from_path

def convert_pdfs_to_pngs():
    # Get the directory of the current script
    dir_path = os.path.dirname(os.path.realpath(__file__))

    # List all PDF files in the directory
    pdf_files = [f for f in os.listdir(dir_path) if f.endswith('.pdf')]

    # Convert each PDF to a PNG image
    for pdf_file in pdf_files:
        try:
            # Generate path for output based on the PDF file name
            output_path = os.path.join(dir_path, os.path.splitext(pdf_file)[0] + '.png')

            # Convert PDF to image
            images = convert_from_path(os.path.join(dir_path, pdf_file))

            # Save the first page as a PNG (or modify this to handle multiple pages)
            for i, image in enumerate(images):
                # Create an output folder if it doesn't exist
                output_folder = os.path.join(dir_path, 'output')
                os.makedirs(output_folder, exist_ok=True)

                # Save the image to the output folder
                image.save(os.path.join(output_folder, os.path.splitext(pdf_file)[0] + f'_{i+1}.png'), 'PNG')

            # Print message for each converted PDF
            print(f"Converted {pdf_file} to PNG.")
        except Exception as e:
            # Handle the exception
            print(f"Error converting {pdf_file}: {str(e)}")

    # Print message when all files are converted
    print("All PDF files converted to PNG.")

# Call the function
if __name__ == '__main__':
    convert_pdfs_to_pngs()