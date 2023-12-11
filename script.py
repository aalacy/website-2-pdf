from bs4 import BeautifulSoup
import requests
from weasyprint import HTML
import pdb

# Website URL
cover_url = ""
url = ""
base_url = ""
size = 26
title="The "

content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>

        <style>
            @page {
                size: A4;
            }

            .page-break {
                page-break-after: always;
            }
        </style>
</head>
<body>
"""

# Scrape Cover
print('Scrape Cover')
response = requests.get(cover_url)
soup = BeautifulSoup(response.content, "lxml")
content += "<center>" + str(soup.select_one('div.u_book_view img')) + "</center><div class='page-break'></div>"

# Get the HTML content
print("Get the HTML content")
for page in range(0, size+1):
    response = requests.get(url.format(page=page))
    soup = BeautifulSoup(response.content, "lxml")
    # Find the table
    table = soup.find('table')
    if page == 0:
        content += "<div align='center'><center>"
    content += str(table)
    if page == 0:
        content += "</center></div><div class='page-break'></div>"
    print('page ', page)

content += "</body></html>"
# Generate PDF with WeasyPrint
print("Generate PDF with WeasyPrint")
pdf = HTML(string=content, base_url=base_url).write_pdf()

# Save the PDF
print("Save the PDF")
with open(f'./book/{title}.pdf', "wb") as f:
    f.write(pdf)

print("Scraped data and generated PDF with inline styles successfully!")