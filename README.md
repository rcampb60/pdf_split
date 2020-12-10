# pdf_split
Takes input from users and then splits out pages of a pdf file with a new name

This is useful for me as there is a multi-page document I split down manually each month using qpdf.
This script uses pikepdf and automates all the changes I usually carry out.

To use make sure to install pikepdf using pip (pip3 install pikepdf)
Then respond to the input questions, making sure to provide the full path of the file i.e. /user/folder/file.pdf

The script will then spit out each page separately with a new name using the prefix you have chosen.
