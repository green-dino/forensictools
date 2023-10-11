import PyPDF2

def extract_text_and_metadata_from_pdf(pdf_path, save_to_file=False, output_file=None):
    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)
            text = ''
            for page_num in range(pdf_reader.numPages):
                text += pdf_reader.getPage(page_num).extractText()
            
            if save_to_file and output_file:
                with open(output_file, 'w', encoding='utf-8') as file:
                    file.write(text)
                print("Extracted text saved to:", output_file)

            pdf_metadata = pdf_reader.getDocumentInfo()
            return text, pdf_metadata

    except Exception as e:
        return None, str(e)

if __name__ == "__main__":
    pdf_path = input("Enter the path to the PDF file: ")
    save_to_file = input("Do you want to save the extracted text to a file? (y/n): ").lower() == 'y'
    output_file = input("Enter the name of the output file (leave empty if not saving to a file): ").strip()
    
    extracted_text, pdf_metadata = extract_text_and_metadata_from_pdf(pdf_path, save_to_file, output_file)
    
    if extracted_text:
        print("Extracted Text:\n")
        print(extracted_text)
        
        if pdf_metadata:
            print("\nPDF Metadata:")
            for key, value in pdf_metadata.items():
                print(f"{key}: {value}")
    else:
        print("Error extracting text from the PDF.")
