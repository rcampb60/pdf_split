from pikepdf import Pdf

location = input("Please tell me where the pdf is located: ")
filename = input("What is the pdf called? ")
new_filename = input("What would you like to prefix the file with? ")

my_pdf = Pdf.open(location + '/' + filename)

for n, page in enumerate(my_pdf.pages, 1):
    dst = Pdf.new()
    dst.pages.append(page)
    dst.save(f'{location}/{new_filename}{n:02d}.pdf')
