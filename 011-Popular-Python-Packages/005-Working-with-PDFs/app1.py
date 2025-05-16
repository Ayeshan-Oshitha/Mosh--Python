import PyPDF2

# Open the original PDF file in read-binary mode
with open("Files5/first.pdf", "rb") as file:
    reader = PyPDF2.PdfReader(file)  # Create a PDF reader object
    print(len(reader.pages))  # Print the number of pages in the PDF

    page = reader.pages[0]
    page.rotate(90)

    writer = PyPDF2.PdfWriter()  # Create a PDF writer object
    writer.add_page(page)  # Add the rotated page to the writer

    # Save the rotated page to a new PDF file
    with open("Files5/rotatedPDF.pdf", "wb") as output:
        writer.write(output)  # Write the modified page to the output file
