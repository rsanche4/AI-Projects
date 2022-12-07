from PyPDF2 import PdfReader
import re

# 1
abbr = 'NLP'
full_text = 'Natural Language Processing'
print(f'{abbr} stands for {full_text}')

# 2
file = open('contacts.txt', 'w+')
file.write('First_Name, Last_Name, Title, Extension, Email')

# 3
fields = file.read()
file.close()
print(fields)

# 4
pdf_loc = '..\\Material\\00-Python-Text-Basics\\Business_Proposal.pdf'
reader = PdfReader(pdf_loc)
page = reader.pages[1]
print(page.extract_text())

# 5
contacts_file = open('contacts.txt', 'a')
removed_authors = page.extract_text().replace('AUTHORS:', '')
contacts_file.write(removed_authors)

# 6
pattern= r'[\w]+@[\w]+.\w{3}'
found = re.findall(pattern, removed_authors)
print(found)