import sys
import os
from PyPDF2 import PdfReader

input_folder = '../Input'

# Force stdout to use UTF-8
sys.stdout.reconfigure(encoding='utf-8')

for file in os.listdir(input_folder):
    if file.endswith('.pdf'):
        print(f"\n=== {file} ===\n")
        reader = PdfReader(os.path.join(input_folder, file))
        for page in reader.pages:
            text = page.extract_text()
            print(text)

