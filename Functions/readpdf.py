import PyPDF2

# This script is useful for quickly extracting text and metadata from PDF files, which can be helpful for data analysis, content extraction, and cataloging.
# Users can extend the script to perform additional tasks with the extracted text or metadata, such as keyword analysis or metadata-based organization.
# Make sure you have the necessary permissions to access and read the specified PDF file.
# Users can customize the script to suit their specific PDF processing needs.


def read_pdf(file_path):
    try:
        with open(file_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text = ''
            for page_num in range(len(pdf_reader.pages)):
                text += pdf_reader.pages[page_num].extract_text()
            return pdf_reader, text
    except Exception as e:
        return None, str(e)

def save_text_to_file(text, output_file):
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(text)
        print("Extracted text saved to:", output_file)
    except Exception as e:
        print("Error saving text:", str(e))

def extract_metadata(pdf_reader):
    metadata = pdf_reader.info.dictionary
    return metadata

if __name__ == "__main__":
    pdf_path = input("Enter the path to the PDF file: ")
    pdf_reader, extracted_text = read_pdf(pdf_path)
    
    if extracted_text:
        print("Extracted Text:\n")
        print(extracted_text)
        
        save_to_file = input("Do you want to save the extracted text to a file? (y/n): ")
        if save_to_file.lower() == 'y':
            output_file = input("Enter the name of the output file: ")
            save_text_to_file(extracted_text, output_file)
        
        # Extract and display PDF metadata
        pdf_metadata = extract_metadata(pdf_reader)
        print("\nPDF Metadata:")
        for key, value in pdf_metadata.items():
            print(f"{key}: {value}")
    else:
        print("Error extracting text from PDF.")
