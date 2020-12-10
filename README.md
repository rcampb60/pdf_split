# pdf_split
Takes input from users and then splits out each individual page of a multi-page pdf file with a new name and numerical sequence i.e NewPDF01.pdf, NewPDF02.pdf etc.

This is useful for me as there is a multi-page document I split down manually each month using qpdf.
This script uses pikepdf and automates all the changes I usually carry out.

To use make sure to install pikepdf using pip (pip3 install pikepdf)
Then respond to the input questions, making sure to provide the full path for the folder where the file is saved without the last "/" i.e. /user/folder

The script will then spit out each page separately with a new name using the prefix you have chosen.
