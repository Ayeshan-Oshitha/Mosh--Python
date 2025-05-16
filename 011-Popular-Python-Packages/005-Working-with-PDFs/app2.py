import PyPDF2

merger = PyPDF2.PdfMerger()  # Instantiate the PdfMerger object

file_names = ["Files5/first.pdf", "Files5/second.pdf"]

for file_name in file_names:
    merger.append(file_name)  # Append each PDF

merger.write("Files5/combined.pdf")  # Write to a new combined file
merger.close()  # Always close the merger after writing
