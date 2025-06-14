import os
import re
from PyPDF2 import PdfReader
from openpyxl import Workbook

input_folder = '../Input'
output_file = '../Output/extracted_invoices.xlsx'

# Fields to extract
FIELDS = [
    'Invoice Number', 'Order Date', 'Customer Name', 'Phone',
    'Address', 'Total Amount', 'Payment Method', 'Platform'
]

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ''
    for page in reader.pages:
        text += page.extract_text() or ''
    return text

'''def extract_fields(text, platform):
    data = {}
    data['Platform'] = platform

    # Regex-based field extraction (may need adjustments based on your PDFs)
    data['Invoice Number'] = re.search(r'(Invoice\s*(Number|ID)[:\s]*)([A-Z0-9\-]+)', text, re.IGNORECASE)
    data['Order Date'] = re.search(r'Order\s*Date[:\s]*([0-9\-\/]+)', text, re.IGNORECASE)
    data['Customer Name'] = re.search(r'Customer\s*Name[:\s]*([A-Za-z\s]+)', text, re.IGNORECASE)
    data['Phone'] = re.search(r'Phone[:\s]*([\d\-]+)', text)
    data['Address'] = re.search(r'Shipping\s*Address[:\s]*(.+?)\n', text, re.IGNORECASE)
    data['Total Amount'] = re.search(r'Total\s*(Amount)?[:\s]*Rs\.?\s?([\d,\.]+)', text, re.IGNORECASE)
    data['Payment Method'] = re.search(r'Payment\s*Method[:\s]*([A-Za-z\s]+)', text, re.IGNORECASE)

    # Clean up
    for key in list(data.keys()):
        match = data[key]
        if isinstance(match, re.Match):
            data[key] = match.group(match.lastindex)
        elif data[key] is None:
            data[key] = 'NA'

    return data'''



def extract_fields(text, platform):
    data = {}
    data['Platform'] = platform

    if platform == 'Amazon':
        data['Invoice Number'] = re.search(r'Invoice Number\s*:\s*([A-Z0-9\-]+)', text)
        data['Order Date'] = re.search(r'Order Date\s*:\s*([0-9]{2}\.[0-9]{2}\.[0-9]{4})', text)
        data['Total Amount'] = re.search(r'TOTAL:.*?\u20b9.*?([0-9,]+\.\d{2})', text)
        data['Payment Method'] = re.search(r'Mode of Payment\s*:\s*([A-Z]+)', text)
        data['Customer Name'] = re.search(r'Billing Address\s*:\s*\n*([A-Z ]+)', text)
        data['Phone'] = re.search(r'Phone[:\s]*([\d\-xX]+)', text)
        data['Address'] = re.search(r'Billing Address\s*:\s*\n*(.*?)\n[A-Z]+', text, re.DOTALL)

    elif platform == 'Flipkart':
        data['Invoice Number'] = re.search(r'Invoice (Number|No)[:#\s]*([A-Z0-9\-]+)', text)
        data['Order Date'] = re.search(r'Order Date[:\s]*([0-9]{2}-[0-9]{2}-[0-9]{4})', text)
        data['Total Amount'] = re.search(r'TOTAL PRICE\s*:\s*([0-9,]+\.\d{2})', text)
        data['Payment Method'] = re.search(r'Mode of Payment[:\s]*([A-Za-z ]+)', text)
        data['Customer Name'] = re.search(r'Billing Address\s*\n([A-Za-z ]+)', text)
        data['Phone'] = re.search(r'Phone[:\s]*([0-9xX\-]+)', text)
        data['Address'] = re.search(r'Billing Address\s*\n(.*?)\nPhone', text, re.DOTALL)

    # Clean matches
    for key in list(data.keys()):
        match = data[key]
        if isinstance(match, re.Match):
            data[key] = match.group(match.lastindex or 1).strip()
        elif data[key] is None:
            data[key] = 'NA'

    return data


def main():
    wb = Workbook()
    ws = wb.active
    ws.append(FIELDS)

    for file in os.listdir(input_folder):
        if file.endswith('.pdf'):
            path = os.path.join(input_folder, file)
            text = extract_text_from_pdf(path)
            platform = 'Amazon' if 'amazon' in file.lower() else 'Flipkart'
            extracted_data = extract_fields(text, platform)
            ws.append([extracted_data.get(field, 'NA') for field in FIELDS])

    wb.save(output_file)
    print(f"Data extraction complete. Excel saved to: {output_file}")

if __name__ == '__main__':
    main()
